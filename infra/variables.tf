# variable "project_name" {}
# variable "environment" {}
# variable "aws_region" {}
# variable "vpc_cidr" {}
# variable "public_subnet_az1_cidr" {}
# variable "public_subnet_az2_cidr" {}
# variable "private_subnet_az1_cidr" {}
# variable "private_subnet_az2_cidr" {}
# variable "container_port" {}
# variable "domain_name" {}
# variable "subdomain_name" {}
# variable "db_name" {}
# variable "db_username" {}
# variable "db_password" {}

variable "project_name" {
  type = string
}

variable "environment" {
  type = string
}

variable "aws_region" {
  type = string
}

variable "vpc_cidr" {
  type = string
}

variable "public_subnet_az1_cidr" {
  type = string
}

variable "public_subnet_az2_cidr" {
  type = string
}

variable "private_subnet_az1_cidr" {
  type = string
}

variable "private_subnet_az2_cidr" {
  type = string
}

variable "container_port" {
  type = number
}

variable "domain_name" {
  type = string
}

variable "subdomain_name" {
  type = string
}

variable "db_name" {
  type = string
}

variable "db_username" {
  type = string
}

variable "db_password" {
  type      = string
  sensitive = true
}