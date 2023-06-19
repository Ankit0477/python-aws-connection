{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "4ea9ac36",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: boto3 in c:\\microsoft\\anaconda\\lib\\site-packages (1.26.155)\n",
      "Requirement already satisfied: s3transfer<0.7.0,>=0.6.0 in c:\\microsoft\\anaconda\\lib\\site-packages (from boto3) (0.6.1)\n",
      "Collecting botocore<1.30.0,>=1.29.155\n",
      "  Using cached botocore-1.29.155-py3-none-any.whl (10.9 MB)\n",
      "Requirement already satisfied: jmespath<2.0.0,>=0.7.1 in c:\\microsoft\\anaconda\\lib\\site-packages (from boto3) (1.0.1)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.25.4 in c:\\microsoft\\anaconda\\lib\\site-packages (from botocore<1.30.0,>=1.29.155->boto3) (1.26.4)\n",
      "Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in c:\\microsoft\\anaconda\\lib\\site-packages (from botocore<1.30.0,>=1.29.155->boto3) (2.8.1)\n",
      "Requirement already satisfied: six>=1.5 in c:\\microsoft\\anaconda\\lib\\site-packages (from python-dateutil<3.0.0,>=2.1->botocore<1.30.0,>=1.29.155->boto3) (1.15.0)\n",
      "Installing collected packages: botocore\n",
      "  Attempting uninstall: botocore\n",
      "    Found existing installation: botocore 1.29.76\n",
      "    Uninstalling botocore-1.29.76:\n",
      "      Successfully uninstalled botocore-1.29.76\n",
      "Successfully installed botocore-1.29.155\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.\n",
      "aiobotocore 2.5.0 requires botocore<1.29.77,>=1.29.76, but you have botocore 1.29.155 which is incompatible.\n"
     ]
    }
   ],
   "source": [
    "!pip install boto3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "cc3b0905",
   "metadata": {},
   "outputs": [],
   "source": [
    "import boto3\n",
    "import pandas as pd\n",
    "\n",
    "s3 = boto3.client('s3')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "48ea1f54",
   "metadata": {},
   "outputs": [],
   "source": [
    "s3 = boto3.resource(\n",
    "    service_name='s3',\n",
    "    region_name='us-east-2',\n",
    "    aws_access_key_id='AKIAQEULWOYNXHTL3V7Q',\n",
    "    aws_secret_access_key='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'\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "cdb19ef5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "source-macys\n",
      "target-macys\n"
     ]
    }
   ],
   "source": [
    "# Print out bucket names\n",
    "for bucket in s3.buckets.all():\n",
    "    print(bucket.name)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1c70b3d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3dc7cab",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "f0da0a7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "\n",
    "# Make dataframes\n",
    "foo = pd.DataFrame({'x': [1, 2, 3], 'y': ['a', 'b', 'c']})\n",
    "bar = pd.DataFrame({'x': [10, 20, 30], 'y': ['aa', 'bb', 'cc']})\n",
    "\n",
    "# Save to csv\n",
    "foo.to_csv('foo.csv')\n",
    "bar.to_csv('bar.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "958b27b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Upload files to S3 bucket\n",
    "s3.Bucket('source-macys').upload_file(Filename='foo.csv', Key='foo.csv')\n",
    "s3.Bucket('source-macys').upload_file(Filename='bar.csv', Key='bar.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "4e5dd8c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Load csv file directly into python\n",
    "obj = s3.Bucket('source-macys').Object('foo.csv').get()\n",
    "foo = pd.read_csv(obj['Body'], index_col=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "1f273863",
   "metadata": {},
   "outputs": [],
   "source": [
    "obj = s3.Bucket('source-macys').Object('bar.csv').get()\n",
    "foo = pd.read_csv(obj['Body'], index_col=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "3f99a574",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>10</td>\n",
       "      <td>aa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>20</td>\n",
       "      <td>bb</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>30</td>\n",
       "      <td>cc</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    x   y\n",
       "0  10  aa\n",
       "1  20  bb\n",
       "2  30  cc"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "foo.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "c62beb98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>x</th>\n",
       "      <th>y</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>a</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>b</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>c</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   x  y\n",
       "0  1  a\n",
       "1  2  b\n",
       "2  3  c"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Download file and read from disc\n",
    "s3.Bucket('source-macys').download_file(Key='foo.csv', Filename='foo2.csv')\n",
    "pd.read_csv('foo2.csv', index_col=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7f2d5ea",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
