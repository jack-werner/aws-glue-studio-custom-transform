output "json_file" {
  description = "json file containing the transformation configuration"
  value       = aws_s3_object.json
}

output "python_file" {
  description = "python file containing the transformation logic"
  value       = aws_s3_object.python
}