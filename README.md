# FalconHit

A secure, multi-layer cascade encryption utility written in Python. This tool applies an aggressive **100-stage cryptographic pipeline** over targeted asset blocks, alternating deterministically through deep implementation layers of industry-standard symmetric primitives.

## Cryptographic Architecture

- **100 Cascade Iterations:** Every target asset passes through 100 distinct encryption stages based on an absolute mathematical sequence.
- **Multi-Cipher Mix:** Dynamically switches and wraps data matrices using:
  - **AES-256-CBC** (with automated padding verification blocks)
  - **ChaCha20** (Stream matrix utilizing unique cryptographic nonces)
  - **Fernet Seals** (Ensuring complete integrity verification)
- **Anti-Vanishing Protections:** Includes gradient mitigation properties such as localized binary clipping bounds during key distribution passes.
- **10-Pass Key Serialization Stack:** Key matrix metadata maps are flattened and passed through an intensive 10-stage sequential string encoding process alternating between Base64 and Base32.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed along with the required low-level cryptographic library dependencies:

```bash
pip install pycryptodome cryptography
```

### How to Run

Launch the secure terminal console link by executing the main script:

```bash
python file_encrypter.py
```

### Operation Vectors
1. **Execute Symmetric Cascade Lock:** Triggers the native OS file picker window. Select the file you wish to lock. The script encrypts the target in place and saves a mutated `.fhit` token key map beside it.
2. **Execute Asset Recovery Matrix:** Select the encrypted file to systematically reverse all 100 loops in absolute mathematical inverse sequence back into the original raw byte blocks.
3. **Disconnect Console:** Safely flushes session volatile memory data and exits.
