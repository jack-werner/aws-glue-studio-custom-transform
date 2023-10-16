# Overview
This repo provides a starting point for a scalable solution for hosting and deploying custom Glue Studio Visual Transforms. Following the guide in this readme will show you how to:

- Build your own custom visual transforms
- Write unit tests to ensure safety of your transforms
- Use GitHub and Terraform module to deploy the transforms
- Use your new transform in Glue Studio

## Getting Started

1. Clone this repo to your local environment
2. Install the requirements
    - This repo uses Apache Spark so you will need to have Java installed. You can follow the docs here ADD LINK to download Java
    - Install the Python packages by running
    `pip install -r requirements.txt` 
    - This repo uses terraform but you don't need it on you local machine to be able to use this repo effectively


## Creating Custom Transforms

There are two files that you need in order to create your custom Glue Studio Visual Transforms, a JSON config file and a Python script containing your transformation logic. You must make sure that both files share the same name (besides their extension), This is how Glue knows to associate them. To use the Terraform module to deploy the transforms you also need to have the files located in the same parent directory. See how the `case_transform` files are named. 

If you want to create addition transforms I would recommend adding them in a directory like `transforms/your_new_transform/your_new_transform.json` and `transforms/your_new_transform/your_new_transform.py`.  

You can review the documentation [here](https://docs.aws.amazon.com/glue/latest/ug/custom-visual-transform-json-config-file.html) to see all the attributes you can configure to customize your transform.

### How the Transform works

The custom transform works by appending our custom transform method to the AWS Glue DynamicFrame class. This is done in the last line of our script

```python
DynamicFrame.case_transform = case_transform
```

Of course for your custom transforms you are can use the built in methods for DynamicFrames outlined [here](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html), but there are visual transforms that correspond to nearly all of these in the Glue Studio UI already, so usually you are probably going to want to convert the DynamicFrame to a Spark DataFrame to get access to the lower level transform capabilities available in Spark. To convert the DynamicFrame to a DataFrame, just call `self.toDF()` like this we do in the `case_transform.py` file:

```python
df: DataFrame = self.toDF()
```

## Testing Your Transforms

This repo uses `pytest` to test the Python transformation function. You can see in the `case_transform.py` file that I have broke out the transformation logic to only use the Spark API. That is so that you can unit test the transformation logic neatly without having to worry about mocking the AWS Glue DynamicFrame types since that code cannot be run locally. The function that actually gets called is only converting the dynamic frame to a DataFrame, passing it to the transform function, and then converting that dataframe back to a dynamic frame. I would recommend that you follow a similar pattern when developing your own custom transforms so that you can keep your unit tests simple and ensure they are rigirously testing values instead of writing weaker assertions with mocks. 

We do several parameter validation checks in our `transform` function before we actually transform any of our data, so we are going to need to write tests that assure all of those errors get raised correctly when invalid parameters are used in addition to checking the columns case gets transformed as expected.

You can run your tests with the command
```
python -m pytest --cov=transforms
```

and you can view the coverage report to see which lines of code are not covered
by running 
```
coverage report -m
```

Here's what the output should look like from the initial code:

![coverage report](img/coverage.png "Coverage Report")

The `Missing` column indicates which lines of code are not covered by the tests that were run. If you look at the `case_transforms.py` file you'll see that those lines are only the ones that deal with converting the DynamicFrame to a DataFrame and back, which we didn't want to test. If you did want to increase your coverage you could of course write new tests for the `case_transform` method that mocked the `DynamicFrame` class.


## Github Actions for Terraform deployment

The setup to integrate Terraform with your AWS account and GitHub repo is out of scope for this readme, but if you do not already have an existing workflow with Terraform I would recommend following the setup guide [here](https://developer.hashicorp.com/terraform/tutorials/cloud-get-started) for using Terraform Cloud with the VCS workflow since it is the easiest to get started with.

Once you have your Terraform workspace set up and connected to your AWS account, see 
`main.tf` to see how to use the module to make it easy to add your transforms to your AWS account. Adding your new custom transform would look something like this

```terraform
module "your_new_transform_name" {
  source     = "./tf_modules/custom_glue_studio_transform/"
  region     = "your-region"
  account_id = "your-aws-account-id"
  filename   = "your_new_transform"
  local_path = "transforms/your_new_transform"
}
```

## Using Your Custom Transform in Glue Studio