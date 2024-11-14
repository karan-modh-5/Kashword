# Kashword

## Overview

Kashword is an innovative approach to reclaim control of your passwords without relying on password managers. In today’s world, many people either reuse the same password or use the same logic across multiple accounts, which creates a significant risk. If your password gets leaked or shared, others can access your accounts. Many turn to password managers to mitigate this risk, but this solution comes with its own set of problems, like the risk of the password manager getting hacked.

**Kashword** addresses these concerns by allowing users to generate unique, secure hashes that can be used as passwords. Since Kashword operates client-side, even if a website uses a weak or no hashing algorithm, they would only receive the hash password you generated. Additionally, you can securely share a hash with others for common accounts, ensuring they only access the intended account without compromising your other accounts.

## How It Works

1. **Hashing Algorithm**: Select the algorithm that will be used to generate the password hash (e.g., SHA-256, SHA-512, etc.).

2. **Kashword Length**: Define how long you want the final hashed password to be. This ensures your passwords can meet different website requirements.

3. **Unique Parameters**: Set a unique starting point or logic to generate your Kashword, making each generated password distinctive.

4. **Use Anywhere**: Even without the Kashword tool, you can recreate your password by using any online hashing service, as long as you know your unique parameters.

## Security Features

- **Protection Against Password Leaks**: Even if a website stores your password in plaintext or uses weak encryption, what they’ll get is the hashed version, providing an additional layer of security.
  
- **Account-Level Sharing**: If you need to share an account, you can safely share a unique hash. The recipient will only have access to that specific account, and your other accounts will remain secure.

- **Offline Generation**: Since Kashword is based on a hashing algorithm and unique logic, you can generate it without an internet connection. There’s no central database or password manager involved.

## Use Cases

- **Common Accounts**: Share Kashwords with others for shared accounts without compromising the security of your other accounts.
  
- **Secure Password Management**: Use same cyphered passwords logic for each account without needing to remember dozens of passwords, all while maintaining high security.

## Why Kashword?

1. **Eliminate Dependency on Password Managers**: By using client-side hashing, you eliminate the need to trust third-party password managers, reducing the risk of widespread password breaches.

2. **Enhanced Security**: Kashword protects against:
   - **Rainbow table attacks**
   - Weak or nonexistent hashing algorithms on websites

3. **Customizable**: Kashword offers a high degree of flexibility by allowing you to:
   - Choose the hashing algorithm (e.g., SHA-512, SHA-256, etc.)
   - Specify the length of the generated Kashword (hashed password)
   - Set a unique starting point for generating your hash

4. **Control and Share Securely**: You can share your Kashword (hash) with others for specific accounts without compromising the security of other accounts. Even if you use the logic behind the hash generation, they will only have access to the shared account.

5. **Universal and Offline**: Since Kashword is based on a logic you define, you don't even need the Kashword tool itself. As long as you remember your parameters and logic, you can generate your Kashword using any online hashing tool. What sets Kashword apart is its serverless architecture. There's no backend connection, ensuring your unique logic never leaves your system. This design choice is crucial for maintaining privacy and security, as it minimizes the risk of data breaches.

## Features

- **Available Across Platforms**: Use Kashword as a Python script, a web-based tool, or a browser extension.
- **Customizable Password Generation**: Adjust password length, starting point, and hashing algorithm to suit your needs.
- **Multiple Hashing Algorithms**: Choose from a variety of algorithms supported by Python's `hashlib` or as provided by the webpage/browser extension.
- **Interactive and Secure Input**: Input passphrases securely, with options for masked input.
- **ASCII Art Logos and Progress Bar**: Enhance your experience with a stylish loading effect and visual progress indicators.
- **Version Information**: Always know which version of Kashword you're using.

--- 

## Conclusion

Kashword is not a product but an **idea** to empower users to take control of their passwords, providing strong protection against password-based attacks. With Kashword, you’re not only securing your accounts but also freeing yourself from the risks associated with password managers.

---

## Platforms

### 1. [Python Script](https://github.com/karan-modh-5/Kashword/blob/main/kashword.py)
Run Kashword locally on your computer for advanced password customization and offline usage.

### 2. [Webpage](https://karan-modh-5.github.io/Kashword/)  
Access Kashword directly from your browser, with an intuitive interface for quick and convenient password generation.

### 3. [Browser Extension](https://microsoftedge.microsoft.com/addons/detail/kashword-generator/jolloicfnlnaeghkmddnpmlhdbenhifk)
Install Kashword as a browser extension for Edge (and compatible browsers) to seamlessly generate passwords while browsing.

---

## Installation and Usage

### Python Script

#### Requirements
- Python 3.x
- Standard Python libraries (`time`, `hashlib`, `sys`, `getpass`, `random`, `string`, `math`, `argparse`, `shutil`, `os`).

#### Installation
Clone the repository or download the script.

#### Usage
Run the script from the command line with optional arguments:
```bash
python kashword.py
```

### Command Line Arguments

- `-v` : Display the version of Kashword.
- `-l <int>` : Specify the password length. 
- `-c <string>` : Provide the passphrase/cypher.
- `-c` : Enter the cypher in clear text.
- `-P` : Disable password masking
- `-s` : Set the starting point for password generation.

---

### Configuration (Python Script)
You can adjust default parameters within the script:

- `length` : Set the default password length.
- `start_from` : Specify the starting position in the hash.
- `algorithm` : Define the default hashing algorithm (e.g., SHA256, SHA512).
- `loading_time` : Customize the time delay for visual effects.

#### *Note:* we always recommend you to use Kashword python script if not possible then use the Kashword website. Other options are also safe and reliable, but the python script gives you more control and flexibility over the password generation process.

If you want to take your security to the next level, you should check out Pashword. It uses Scrypt and SHA3-512 on multiple user inputs, which makes it much harder to brute-force. 
https://pashword.app/
