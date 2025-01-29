import requests
import json

def scan_vulnerabilities(target_url):
    """
    Simulated AI-based vulnerability scanner.
    :param target_url: The URL to scan for vulnerabilities.
    :return: A report of found vulnerabilities.
    """
    # Simulated scan process
    vulnerabilities = [
        {"id": "CVE-2023-1234", "severity": "High", "description": "SQL Injection vulnerability detected."},
        {"id": "CVE-2023-5678", "severity": "Medium", "description": "Outdated library version found."}
    ]
    
    return {
        "target": target_url,
        "status": "Scan complete",
        "vulnerabilities": vulnerabilities
    }

def integrate_with_cicd(scan_report, webhook_url):
    """
    Send the scan report to a CI/CD pipeline via a webhook.
    :param scan_report: The vulnerability scan report.
    :param webhook_url: The CI/CD webhook URL to send data.
    """
    headers = {'Content-Type': 'application/json'}
    response = requests.post(webhook_url, data=json.dumps(scan_report), headers=headers)
    
    if response.status_code == 200:
        return "Report successfully sent to CI/CD pipeline."
    else:
        return f"Failed to send report. HTTP Status: {response.status_code}"

if __name__ == "__main__":
    # Example usage
    target = "https://example.com"
    ci_cd_webhook = "https://cicd-pipeline.example.com/webhook"
    
    report = scan_vulnerabilities(target)
    print(json.dumps(report, indent=4))
    
    result = integrate_with_cicd(report, ci_cd_webhook)
    print(result)


# TODO: Supprimer avant le push !!!
# access_token = "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"  

import requests

def fetch_private_repo():
    headers = {"Authorization": f"Bearer {'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'}"}  # Fixme: ne pas hardcoder
    response = requests.get("https://gitlab.com/api/v4/projects/123/repository", headers=headers)
    return response.json()

print(fetch_private_repo())



git push 
