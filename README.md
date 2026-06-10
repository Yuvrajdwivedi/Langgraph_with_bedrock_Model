# AWS-Infrastructure-Automation
Build an end-to-end AWS EC2 setup spanning Windows and Amazon Linux environments.  
Infrastructure Overview:  
1. Windows EC2: Configured with RDP access, Security Group rules (port 3389 + app ports), IAM roles, and EBS encryption
2. Linux EC2: Set up with PuTTY/MobaXTerm access, replicated security configurations
3. Elastic IPs: Assigned to both instances for persistent connectivity
4. Automation: AWS SSM Quick Setup → Lambda → EC2 tag-based scheduling (9-5, Mon-Fri)
Stack: AWS EC2, Security Groups, IAM, KMS Encryption, EBS, Elastic IPs, Systems Manager, Lambda
The project reinforced a critical lesson: infrastructure is only as strong as its security posture and automation layer. Combining granular IAM policies, encryption, and intelligent scheduling creates scalable, cost-optimized systems.
