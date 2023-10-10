terraform {

  # cloud {
  #     organization = "jack-werner-personal"

  #     workspaces {
  #         name = "aws-glue-studio-custom-transform"
  #     }
  # }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.20.0"
    }
  }

  required_version = ">= 0.14.0"
}