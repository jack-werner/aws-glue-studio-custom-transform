terraform {

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.20.0"
    }
  }

  required_version = ">= 0.14.0"
}