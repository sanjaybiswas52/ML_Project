from mylibrary import file_conversion as mylib

mylib.convert_doc_to_text('/Users/sanjaybiswas/Downloads/ATS-G-1807-AJAY RAJ WAZIR-A.docx', '/Users/sanjaybiswas/Downloads/ATS-G-1807_sanjay.text')
from cosmos.operators import DbtDocsS3Operator

# then, in your DAG code:
generate_dbt_docs_aws = DbtDocsS3Operator(
    task_id="generate_dbt_docs_aws",
    project_dir="path/to/jaffle_shop",
    profile_config=profile_config,
    # docs-specific arguments
    connection_id="test_aws",
    bucket_name="test_bucket",
)