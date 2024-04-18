# Reproducibility 

## Step 1 Set Up Kaggle Credentials


- Log into a [Kaggle](https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F) 

- Go to your Account > Settings > API section 

Click Create New Token:
  
 
A JSON file with a username and key will be generated:

```
{
  "username": "<your_kaggle_username>",
  "key": "<your_kaggle_key>"
}

```

Save this JSON file somewhere on your local machine. 

Note: We’ll use this infor when installing Mage on our VM in Google cloud, **Step 5**, where we’ll add username & key from the generated JSON file to the .env file.
```
kaggle_username = "< your_kaggle_username >"
kaggle_key = "< your_kaggle_key >"
```


## Step 2  - Set-Up GCP Project & Service Account Credentials


- [Log in ](https://console.cloud.google.com/) into Google Cloud Platform (GCP) console. 


- Create a new project in the GCP console. 

Give the new project a name (I called mine zoom-de-project) 
Make note of the Project ID (mine is zoom-de-project-id2). 
 
This Project ID will be needed later on (fill in where) to replace the PROJECT_ID with your own project ID.


- Create an IAM Service account 

(I called mine zoom-de-service-account)
 
Press Create And Continue & set up the following roles:

- ** BigQuery Admin**
- **Storage Admin**
- **Storage Object Admin**
- **Viewer**

 
- Create Service Account key 

 
Download the Service Account Key and store it in $HOME/.gc /

```
$HOME/.gc /gcp_auth.json
```

We need to activate the following [APIs](https://cloud.google.com/apis)

-	**Cloud Storage API**  
-	**BigQuery API** 
-	**Compute Engine API**
-	**Identity and Access Management (IAM) API**
-	**IAM Service Account Credentials API**


## Step 3 - Create SSH Keys to Access VM

SSH key used to login to our GCP VM instance.

In the GCP console, choose Compute Engine from the left menu
Then access Metadata and proceed to the SSH KEYS tab.

 
Click on the ADD SSH KEY button.


Paste the public key into the designated field and save your changes by clicking the SAVE button.

For Windows 10

1.	Open the Windows 10 Start menu and search for “Apps & Features”. 
In the “Apps & Features” heading, click “Optional Features”.
 
2.	Scroll down the list to see if “OpenSSH Client” is listed.  If not, click the plus sign next to “Add a feature”, select OpenSSH Client, and click “Install”.
 


## Step 4  Create VM

 
1.	From your project's dashboard, go to Cloud Compute > VM instance
2.	Create a new instance:
-	Choose name de-project-vm
-	Pick Region europe-west2 (London)
-	Pick Zone europe-west2-c
-	Pick a E2 series instance. I went with a e2-highmem-4 (4 vCPU, 2 core, 32 GB memory)
-	Change the boot disk to Ubuntu. The Ubuntu 20.04 LTS version & choose 30GB of storage.
-	Leave all other settings on their default value and click on Create.


## Step 5 - Install Packages on GCP VM Instance

### Step a: SSH into your VM 
### Step b: Clone GitHub project repo
```
$ git clone https://github.com/BarrCoder2024/movie_lens_batch_de_project  zoom-project 
$ cd zoom-project
```
### Step c: Set environment variables for authorisation

Setup a JSON file:
```
	$ mkdir -p ~/.gc
	$ touch ~/.gc/gcp_auth.json
	$ nano ~/.gc/gcp_auth.json
```
[Note:  ctrl + O to save ctrl+X to exit]

Create copy for docker:
```
$ cp ~/.gc/gcp_auth.json ~/zoom-project/mage-spark/gcp_auth.json
```

Activate environment Variables:
```
$ echo 'export GOOGLE_APPLICATION_CREDENTIALS=~/.gc/gcp_auth.json' >> ~/.bashrc 
$ . ~/.bashrc
```
### Step d: Install Docker
```
$ cd ~  
$ sudo apt-get update  
$ sudo apt-get install -y docker.io 
$ sudo service docker.io restart
```

### Step e: Install Docker compose 

```
$ mkdir bin 
$ cd bin  
$ sudo wget https://github.com/docker/compose/releases/download/v2.26.1/docker-compose-linux-x86_64 -O  docker-compose  
$ sudo chmod +x docker-compose 
$ cd ~ 
$ echo 'export PATH="${HOME}/bin:${PATH}"' >> .bashrc 
$ . ~/.bashrc
$ sudo service docker restart
```

### Step f: Install Terraform

```
$ cd bin 
$ wget https://releases.hashicorp.com/terraform/1.8.0/terraform_1.8.0_linux_amd64.zip 
$ sudo apt-get install unzip
$ unzip terraform_1.8.0_linux_amd64.zip 
$ rm terraform_1.8.0_linux_amd64.zip
```

## Step 6 – Start up

Step 1: Using Terraform to set up GCS & BQ
#To initiate, plan and apply the necessary infrastructure, please execute the following Terraform commands, adjusting as needed. Please provide the ID of your project.
```
$ cd ~/zoom-project/terraform/
```
[NEED TO ADD NANO THE VARIABLES FILE FOR TERRAFORM ID]
```
$nano variables.tf
```
input “project id” bucket names etc
```
$ terraform init
$ terraform plan   
$ terraform apply 
``` 
Step 2: Build Mage docker image with Spark environment
#Add information about your Kaggle API token and gcloud project ID
```
$ cd ~/zoom-project/
$ mv dev.env .env
$ nano .env
```
# Build Mage docker image with Spark environment
```
$ docker build -t mage_spark .
```
# Start Mage using docker
```
$ docker run -it --name mage_spark -e SPARK_MASTER_HOST='local' -p 6789:6789 -v $(pwd):/home/src mage_spark  /app/run_app.sh mage start mage-spark-zoom
```
