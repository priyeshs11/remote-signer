# Tezos Remote Signer Fork 

Forked from [https://github.com/tacoinfra/remote-signer](url)

This is a Python Flask app that receives messages from the Tezos baking client and passes them on to a remote HSM to be signed. This software uses the [py-hsm module](https://github.com/bentonstark/py-hsm) to support PKCS#11 signing operations, which means it should support the following HSMs:

* Gemalto SafeNet Luna SA-4
* Gemalto SafeNet Luna SA-5
* Gemalto SafeNet Luna PCIe K5/K6
* Gemalto SafeNet Luna CA-4
* SafeNet ProtectServer PCIe
* FutureX Vectera Series
* Cavium LiquidSecurity FIPS PCIe Card
* Utimaco Security Server Simulator (SMOS Ver. 3.1.2.3)
* OpenDNSSEC SoftHSM 2.2.0 (softhsm2)

Note that we have only tested it on [AWS CloudHSM](https://aws.amazon.com/cloudhsm/), which is based on the Cavium LiquidSecurity FIPS PCIe Card.

## Security Notes

Please note that this software does not provide any authentication or authorization. You will need to take care of that yourself. It simply returns the signature for valid payloads, after performing some checks:
* Is the message a valid payload?
* Does the message begin with a 0x01 or 0x02 or 0x03? Indicating it is a baking, endorsement or a transfer.
* Is the message within a certain threshold of the head of the chain? Ensures you are signing valid blocks.
* For baking signatures, is the block height of the payload greater than the current block height? This prevents double baking.

## Installation

Please note that you will need to install and compile your vendor's PKCS#11 C library before the py-hsm module will work.

You can use the following commands to install Python3.

```
sudo apt-get update
sudo apt-get -y install python3-pip
```

Download the application repository using git clone:

```
git clone https://github.com/priyeshs11/remote-signer.git
```

To install required modules, use pip with requirements.txt provided.

```
cd remote-signer
pip3 install -r requirements.txt
```

Create a .env file with the same variables as in .env.example.
```
cp .env.example .env 
```
Create a keys.json file with the same structure as in keys.json.example.
```
cp keys.json.example keys.json
```

Complete the .env and keys.json file with your credentials and keys using the editor of your choice.

## Execution
```
python3 signer.py
```
To run in backgrund:
```
nohup python3 signer.py > signer.out &
```

## Running the tests
```
python -m unittest test/test_remote_signer.py
```