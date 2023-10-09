terraform {

    # cloud {
    #     organization = "jack-werner-personal"

    #     workspaces {
    #         name = "aws-glue-studio-custom-transform"
    #     }
    # }

    required_providers {
      aws = {
        source = "hashicorp/aws"
        version = "~> 3.28.0"
      }
    }

    required_version = ">= 0.14.0"
}