# Use the official AWS Lambda Python 3.12 base image.
FROM public.ecr.aws/lambda/python:3.12

# Copy requirements and install them.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project code into the image.
COPY . ${LAMBDA_TASK_ROOT}

# Set the CMD to your Lambda handler (adjust the module and handler function name).
# In this example, the Lambda handler is defined in 
# com/dimcon/synthera_netsuite_integration/controller/lambda_entry_point.lambda_handler
CMD ["com.dimcon.synthera_netsuite_integration.controller.lambda_entry_point.lambda_handler"]