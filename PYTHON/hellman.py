import os
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization,hashes


def generate_dh_parameters():
    # Generate Diffie-Hellman parameters
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    return parameters

def generate_keys(parameters):
    # Generate a private key for use in the exchange
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def compute_shared_key(private_key, peer_public_key):
    # Compute the shared secret key
    shared_key = private_key.exchange(peer_public_key)
    return shared_key

def measure_performance():
    # Generate Diffie-Hellman parameters
    start_time = time.time()
    parameters = generate_dh_parameters()
    dh_param_time = time.time() - start_time
    print(f"Diffie-Hellman Parameter Generation Time: {dh_param_time:.4f} seconds")

    # Peer A generates keys
    start_time = time.time()
    peer_a_private_key, peer_a_public_key = generate_keys(parameters)
    peer_a_key_gen_time = time.time() - start_time
    print(f"Peer A Key Generation Time: {peer_a_key_gen_time:.4f} seconds")

    # Peer B generates keys
    start_time = time.time()
    peer_b_private_key, peer_b_public_key = generate_keys(parameters)
    peer_b_key_gen_time = time.time() - start_time
    print(f"Peer B Key Generation Time: {peer_b_key_gen_time:.4f} seconds")

    # Peer A computes the shared key using Peer B's public key
    start_time = time.time()
    peer_a_shared_key = compute_shared_key(peer_a_private_key, peer_b_public_key)
    peer_a_shared_key_time = time.time() - start_time
    print(f"Peer A Shared Key Computation Time: {peer_a_shared_key_time:.4f} seconds")

    # Peer B computes the shared key using Peer A's public key
    start_time = time.time()
    peer_b_shared_key = compute_shared_key(peer_b_private_key, peer_a_public_key)
    peer_b_shared_key_time = time.time() - start_time
    print(f"Peer B Shared Key Computation Time: {peer_b_shared_key_time:.4f} seconds")

    # Verify that both peers have the same shared key
    assert peer_a_shared_key == peer_b_shared_key
    print("Shared keys match!")

if __name__ == "__main__":
    measure_performance()
