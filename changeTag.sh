#!/bin/bash
sed "s/tagVersion/$1/g" mydev.yml > my_deployment.yml