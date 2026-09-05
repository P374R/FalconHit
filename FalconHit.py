import os
import sys
import time
import base64
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Low-level cryptographic primitives
from cryptography.fernet import Fernet
from Crypto.Cipher import AES, ChaCha20
from Crypto.Random import get_random_bytes

def pr_out(text, delay=0.001, color="\033[0m"):
    """Handles terminal streaming sequences using optimized agency delays."""
    reset = "\033[0m"
    for char in text:
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def init_shell():
    """Validates secure cryptographic environment initialization parameters."""
    os.system('cls' if os.name == 'nt' else 'clear')
    pr_out("==================================================================", delay=0.001)
    pr_out("[!] SEC-OP // LOCAL ENDPOINT ENTRY // CLASS-A RESTRICTED ACCESS", color="\033[91m")
    pr_out("[!] MULTI-LAYER CASCADE MATRIX OPERATIONAL // CORE-BUILD 12.0.01", color="\033[91m")
    pr_out("==================================================================", delay=0.001)
    time.sleep(0.1)
    pr_out("[*] Mapping cryptographic primitives to volatility array...")
    pr_out("[*] AES-256-CBC, ChaCha20, and Fernet core layers synchronized.")
    pr_out("[+] File ingestion pipeline online.\n")

def acquire_target(mode_str):
    """Triggers standard OS window manager interrupt to allocate target payload."""
    root = Tk()
    root.withdraw()                   
    root.wm_attributes('-topmost', 1) 
    
    pr_out(f"[*] INITIALIZING FILESYSTEM INTERRUPT FOR SEQUENCE: {mode_str}...", color="\033[93m")
    target_file = askopenfilename(title=f"Terminal Handler: Select Asset [{mode_str}]")
    
    root.destroy()                    
    return target_file

def generate_deterministic_sequence(total_stages=100):
    """Generates a stable, repeatable sequence of ciphers using an absolute pattern."""
    sequence = []
    for stage in range(1, total_stages + 1):
        # Combines multiple mathematical offsets to create a highly varied, non-linear pattern
        cipher_type = (stage * 7 + (stage % 4) * 13 + 3) % 3
        sequence.append(cipher_type)
    return sequence

def execute_key_encoding_stack(data):
    """Passes raw matrix data through a randomized 10-stage serialization stack."""
    # 10 passes: B64 -> B32 -> B64 -> B64 -> B32 -> B64 -> B32 -> B32 -> B64 -> B32
    encoding_map = [0, 1, 0, 0, 1, 0, 1, 1, 0, 1]
    
    for process in encoding_map:
        if process == 0:
            data = base64.b64encode(data)
        else:
            data = base64.b32encode(data)
    return data

def execute_key_decoding_stack(data):
    """Unwinds the 10-stage serialization stack in exact reverse order."""
    # Reverse order of the encoding_map
    decoding_map = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
    
    for process in decoding_map:
        if process == 1:
            data = base64.b32decode(data)
        else:
            data = base64.b64decode(data)
    return data

def run_lock():
    """Applies a 100-layer deep cryptographic stack over the targeted asset."""
    target_path = acquire_target("LOCK")
    if not target_path:
        pr_out("[-] PROCESS TERMINATED. NO TARGET SIGNATURE EXPOSED.", color="\033[91m")
        return

    vault_path = target_path + ".fhit"
    if os.path.exists(vault_path):
        os.remove(vault_path)

    pr_out(f"\n[*] TARGET ACQUIRED: {os.path.basename(target_path)}")
    pr_out("[*] Allocating raw byte block memory...")
    
    with open(target_path, "rb") as f:
        payload = f.read()

    key_matrix = bytearray()
    cipher_sequence = generate_deterministic_sequence(100)

    pr_out("[~] EXECUTION VECTOR: RUNNING 100-STAGE CASCADE PIPELINE...", color="\033[32m")
    
    for index, vector in enumerate(cipher_sequence):
        stage = index + 1
        
        if vector == 0:
            if stage % 10 == 0:
                pr_out(f"    [Stage {stage:03d}/100] Applying AES-256 Block Shield Layer...")
            block_key = get_random_bytes(32)
            engine = AES.new(block_key, AES.MODE_CBC)
            init_vector = engine.iv
            
            pad_byte = 16 - (len(payload) % 16)
            payload += bytes([pad_byte] * pad_byte)
            scrambled = engine.encrypt(payload)
            
            payload = init_vector + scrambled
            key_matrix.extend(b"AES:" + block_key)
            
        elif vector == 1:
            if stage % 10 == 0:
                pr_out(f"    [Stage {stage:03d}/100] Applying ChaCha20 Stream Matrix Layer...")
            stream_key = get_random_bytes(32)
            engine = ChaCha20.new(key=stream_key)
            nonce_bytes = engine.nonce
            scrambled = engine.encrypt(payload)
            
            payload = nonce_bytes + scrambled
            key_matrix.extend(b"CHA:" + stream_key)
            
        else:
            if stage % 10 == 0:
                pr_out(f"    [Stage {stage:03d}/100] Applying Fernet Verification Seal Layer...")
            seal_key = Fernet.generate_key()
            engine = Fernet(seal_key)
            payload = engine.encrypt(payload)
            key_matrix.extend(b"FRN:" + seal_key)

    pr_out("[*] Executing 10-stage deep key matrix serialization...")
    encoded_matrix = execute_key_encoding_stack(key_matrix)

    pr_out("[*] Overwriting original filesystem reference with mutated blocks...")
    with open(target_path, "wb") as f:
        f.write(payload)

    with open(vault_path, "wb") as f:
        f.write(encoded_matrix)

    pr_out("\n[+++] MUTATION PROCESS COMPLETE. ASSET BLOCKS SUCCESSFULLY LOCKED [+++]", color="\033[0m")
    pr_out(f"[+] 10-Pass Key map saved to: {os.path.basename(vault_path)}", color="\033[0m")

def run_unlock():
    """Unwinds all 100 cryptographic loops using strict binary offset streaming."""
    target_path = acquire_target("UNLOCK")
    if not target_path:
        pr_out("[-] PROCESS TERMINATED. NO TARGET SIGNATURE EXPOSED.", color="\033[91m")
        return

    vault_path = target_path + ".fhit"
    if os.path.exists(vault_path):
        pass
    else:
        pr_out(f"[-] ACCESS DENIED: KEY VAULT DETACHED ({os.path.basename(vault_path)} MISSING)", color="\033[91m")
        return

    pr_out(f"\n[*] TARGET CAPTURED: {os.path.basename(target_path)}")
    pr_out("[*] Processing cryptographic deployment map tokens...")
    
    with open(vault_path, "rb") as f:
        encoded_matrix = f.read()

    try:
        pr_out("[*] Deserializing 10-stage key matrix encoding stack...")
        raw_matrix = execute_key_decoding_stack(encoded_matrix)
    except Exception:
        pr_out("[-] CRITICAL FAILURE: MATRICIAL ENCODING INTEGRITY COMPROMISED.", color="\033[91m")
        return

    matrix_lines = []
    pointer = 0
    cipher_sequence = generate_deterministic_sequence(100)
    
    try:
        for vector in cipher_sequence:
            prefix = raw_matrix[pointer:pointer+4]
            if prefix.startswith(b"AES:") or prefix.startswith(b"CHA:"):
                matrix_lines.append(raw_matrix[pointer:pointer+36])
                pointer += 36
            elif prefix.startswith(b"FRN:"):
                matrix_lines.append(raw_matrix[pointer:pointer+48])
                pointer += 48
            else:
                break
    except Exception:
        pass

    if len(matrix_lines) != 100:
        pr_out(f"[-] CRITICAL FAILURE: ASSET TOKEN MAP STRUCTURAL CORRUPTION (Found {len(matrix_lines)}/100).", color="\033[91m")
        return

    with open(target_path, "rb") as f:
        payload = f.read()

    try:
        pr_out("[~] DECONSTRUCTING ENCRYPTION CORES (REVERSE STACK SEQUENCE)...", color="\033[32m")
        
        # Unwind the 100 stages in exact reverse order
        for index in range(99, -1, -1):
            stage = index + 1
            vector = cipher_sequence[index]
            token = matrix_lines[index]
            core_signature = token[:3]
            raw_token_key = token[4:]
            
            if core_signature == b"AES" and vector == 0:
                if stage % 10 == 0:
                    pr_out(f"    [Stage {stage:03d}/100] Reversing AES-256 Cipher Block Shield...")
                init_vector = payload[:16]
                enc_payload = payload[16:]
                engine = AES.new(raw_token_key, AES.MODE_CBC, iv=init_vector)
                payload = engine.decrypt(enc_payload)
                
                pad_byte = payload[-1]
                payload = payload[:-pad_byte]
                
            elif core_signature == b"CHA" and vector == 1:
                if stage % 10 == 0:
                    pr_out(f"    [Stage {stage:03d}/100] Reversing ChaCha20 Stream Layer...")
                nonce_bytes = payload[:8]
                enc_payload = payload[8:]
                engine = ChaCha20.new(key=raw_token_key, nonce=nonce_bytes)
                payload = engine.decrypt(enc_payload)
                
            elif core_signature == b"FRN" and vector == 2:
                if stage % 10 == 0:
                    pr_out(f"    [Stage {stage:03d}/100] Reversing Fernet Verification Seal...")
                engine = Fernet(raw_token_key)
                payload = engine.decrypt(payload)
            else:
                raise ValueError("Operational alignment mismatch within cryptographic vector stack.")

        with open(target_path, "wb") as f:
            f.write(payload)

        pr_out("\n[+++] REVERSAL SUCCESSFUL. ORIGINAL DATA MATRIX RECONSTRUCTED [+++]", color="\033[0m")

    except Exception as err:
        pr_out("\n[-] CORE INTERRUPT FAILURE: UNABLE TO DESTRUCTURE TARGET.", color="\033[91m")
        pr_out(f"[-] EXCEPTION VECTOR: {err}", color="\033[91m")

def main():
    init_shell()
    
    print("Select Operation Vector:")
    print("  [1] EXECUTE SYMMETRIC CASCADE LOCK [100 LAYERS]")
    print("  [2] EXECUTE ASSET RECOVERY MATRIX  [100 LAYERS]")
    print("  [3] DISCONNECT CONSOLE TERM LINK")
    
    cmd = input("\nSEC-OP-Node> ").strip()

    if cmd == "1":
        run_lock()
    elif cmd == "2":
        run_unlock()
    elif cmd == "3":
        pr_out("[*] Wiping volatility session memory cache. Flushing footprints. Offline.", color="\033[93m")
    else:
        pr_out("[-] INVALID UTILITY COMMAND. DISCONNECTING ENDPOINT LINK.", color="\033[91m")

if __name__ == "__main__":
    main()