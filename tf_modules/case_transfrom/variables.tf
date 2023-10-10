variable "region" {
  description = "The AWS region to deploy to"
  type = string
}

variable "account_id" {
  description = "Your AWS account id"
  type = string
}

variable "file_name" {
  description = "The name of your json and python files. Do not include filetype extensions."
  type = string
}

variable "source" {
  description = "The local path to your json and python files. Do not include trailing slash."
  type = string
}