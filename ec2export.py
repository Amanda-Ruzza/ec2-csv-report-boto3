import boto3
import csv

# Get the available instances
def Get_Instances():
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances()
    return response['Reservations'][0]['Instances']

# Write the output information into CSV
def CSV_Writer(header, content):
    with open('export.csv', 'w') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=header)
        writer.writeheader()
        for row in content: # the 'writer' will take each row of content, and wrte it to the file
            writer.writerow(row)

if __name__ == "__main__":
    instances = Get_Instances()
    header = ['InstanceId', 'InstanceType', 'State', 'PublicIpAddress']
    data = []
    for instance in instances: # looping through the instances that we get and passing them into the 'writer'
        print(f"Adding instance {instance['InstanceId']} to the CSV file ")
        data.append(
            {
                "InstanceId": instance['InstanceId'],
                "InstanceType": instance['InstanceType'],
                "State": instance['State']['Name'],
                # "PublicIpAddress": instance['PublicIpAddress']
            }
        )
    CSV_Writer(content=data,header=header)


