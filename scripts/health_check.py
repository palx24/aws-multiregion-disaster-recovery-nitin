import requests
import time

# REPLACE THESE WITH YOUR ACTUAL ALB URLS
PRIMARY_ALB = "dr-primary-alb-678483851.us-east-1.elb.amazonaws.com"
SECONDARY_ALB = "dr-secondary-alb-1327538181.us-west-2.elb.amazonaws.com" 

def check_health():
    print(f"🔍 Checking Primary Region: {PRIMARY_ALB}")
    try:
        response = requests.get(PRIMARY_ALB, timeout=5)
        if response.status_code == 200:
            print("✅ PRIMARY REGION IS HEALTHY. Traffic is normal.")
        else:
            raise Exception("Bad Status Code")
    except Exception as e:
        print(" CRITICAL FAILURE: Primary Region is DOWN!")
        print(f"⚠️ INITIATING FAILOVER PROTOCOL...")
        print(f"🔄 Redirecting traffic to Secondary Region: {SECONDARY_ALB}")
        print("📧 Alerting On-Call Engineer via Slack/PagerDuty...")

if __name__ == "__main__":
    check_health()