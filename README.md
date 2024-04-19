# Batch Data Engineering Project - MovieLens 20M Dataset 

The aim of this project was to build an end-to-end data pipeline to ingest a suitably sized dataset into a datalake, performing some transformations to ready the data for storage in a data warehouse and to then build a dashboard to visualise the data.
To that end, I decided to use the MovieLens 20M Dataset, with over 20 million movie ratings and tagging activities, as a suitable foundation for my first ever data engineering project. 

## Prerequisites

- A [Kaggle](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset?select=link.csv) account is required to access the data.
- A [Google Cloud Platform](https://cloud.google.com/) account is necessary as the project relies on Google Cloud's suite of computing services, specifically for storage and compute resources.

## Data Stack Used

- **Data Lake:** [Google Cloud Storage (GCS)](https://cloud.google.com/storage)
- **Data Warehouse:** [BigQuery](https://cloud.google.com/bigquery)
- **Data Transformations:** [Apache Spark](https://spark.apache.org/)
- **Infrastructure as code (IaC):** [Terraform](https://github.com/hashicorp/terraform)
- **Workflow orchestration:** [Mage](https://www.mage.ai/)
- **Containerization:** [Docker](https://www.docker.com/)
- **Visualisation:** [Looker Studio](https://lookerstudio.google.com/)

## Dataset

The MovieLens 20M Dataset contains 20 million ratings and 465,000 tag applications applied to 27,000 movies by 138,000 users. Each rating consists of a user ID, a movie ID, a rating, and a timestamp indicating when the rating was given.
It includes tag genome data with 12 million relevance scores across 1,100 tags. Released 4/2015.



## Dashboard

You can view my dashboard [here](https://lookerstudio.google.com/reporting/75c62ab4-6b6d-41c2-bd5d-980a6cdd8a16).

This dashboard is ideally suited for an upstream audience of data scientists and other stakeholders to provide insights into audience preferences, viewing habits, and community engagement. The dashboard offers actionable data for optimizing content curation, refining recommendation algorithms, and understanding of user interaction with the ratings process.


## Instructions to Run the Code

Instructions to run the code are [here](instructions/instructions.md).

## Acknowledgments

A big thank you to [Alexey Grigorev](https://github.com/alexeygrigorev) and his team for putting together this excellent course, and for making it available to all, free of charge. Creating such a course requires a considerable amount of time and effort, and I'm appreciative of these efforts. I'm very pleased to have been a part of the 2024 cohort of the [DataTalks.Club Data Engineering Zoomcamp](https://datatalks.club/blog/data-engineering-zoomcamp.html). Thank you all!

