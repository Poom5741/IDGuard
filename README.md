# idGuard

idGuard is a decentralized platform for KYC (Know Your Customer) and identity verification built on the Internet Computer Protocol (ICP). The project uses blockchain to securely manage and verify identity data while providing a user-friendly interface for both users and administrators.

## Project Structure

The project is organized into four main components:

```
idGuard/
├── README.md                          # Root documentation
├── identity_canister_project/          # Canister for managing user identities
├── kyc/                                # Canister for managing KYC requests
├── llama_cpp_canister/                 # Canister for LLM integration (planned for future use)
└── verify-id-ui/                       # Frontend interface for user and admin interaction
```

### 1. identity_canister_project/

This directory contains the code for the Identity Canister, which is responsible for handling user identities on the blockchain. It includes:

- **Cargo.toml**: Rust package manager configuration for dependencies.
- **dfx.json**: DFX configuration for deploying canisters.
- **src/**: The main Rust source files for the canister.

### 2. kyc/

This directory contains the KYC Canister, which manages KYC requests (submission, approval, rejection). It ensures the cryptographic signing of documents and stores them on the blockchain. It includes:

- **Cargo.toml**: Rust package manager configuration for dependencies.
- **dfx.json**: DFX configuration for deploying the KYC canister.
- **src/**: Rust source code for the KYC logic, cryptographic signing, and storage.

### 3. llama_cpp_canister/

This directory contains the code for the planned LLM (Large Language Model) Canister integration, which will be used in the future to process and structure OCR data into JSON format. It includes:

- **model.safetensors** and **tokenizer.json**: Model files for natural language processing.
- **Makefile** and **icpp.toml**: Build configurations for compiling the canister.
- **src/**: Source code for the canister logic, allowing interaction with the LLM for document analysis.

### 4. verify-id-ui/

This is the Frontend for the project, built using Next.js. It contains all the necessary files for rendering the user interface and interacting with the canisters. It includes:

- **app/**: The pages for the frontend UI, including KYC management and identity management.
- **components/**: Reusable UI components (built with ShadCN).
- **tailwind.config.ts**: Tailwind CSS configuration for styling.
- **lib/**: Utility functions used across the frontend.

## Installation and Setup

### Prerequisites

Ensure you have the following installed before setting up the project:

- DFX SDK (for deploying canisters on the Internet Computer)
- Rust and Cargo (for building the canisters)
- Node.js and npm (for running the frontend)
- Vercel CLI (optional, for frontend deployment)

### Backend (Canisters)

1. Clone the Repository:

   ```bash
   git clone https://github.com/yourusername/idguard.git
   cd idguard
   ```

2. Deploy Canisters:

   - Start the local Internet Computer (ICP) replica:

     ```bash
     dfx start --background
     ```

   - Deploy both the identity_canister_project and kyc canisters:

     ```bash
     cd identity_canister_project
     dfx deploy

     cd ../kyc
     dfx deploy
     ```

3. Testing Canisters:

   Use DFX to interact with the canisters:

   - Submit a KYC request:

     ```bash
     dfx canister call kyc_backend submit_kyc '("user1", "document data")'
     ```

   - Get the status of a KYC request:

     ```bash
     dfx canister call kyc_backend get_kyc_status '("user1")'
     ```

### Frontend (UI)

1. Navigate to the Frontend Directory:

   ```bash
   cd verify-id-ui
   ```

2. Install Dependencies:

   ```bash
   npm install
   ```

3. Run the Development Server:

   ```bash
   npm run dev
   ```

   The frontend should now be available at [http://localhost:3000](http://localhost:3000).

4. Deploy the Frontend (Optional):

   If using Vercel for deployment, you can deploy the frontend by linking the repository to Vercel and running:

   ```bash
   vercel --prod
   ```

## Future Improvements

1. **LLM Integration**: In future iterations, the project will integrate Large Language Models (LLMs) via the llama_cpp_canister to process OCR data, converting it into structured JSON format for further use in document verification.

2. **Data Pipeline**: Enhancements to the data pipeline are planned to ensure that KYC requests can be processed more efficiently at scale, with automated data routing and storage.

3. **Scalability**: Further focus will be placed on scaling the platform to handle a larger volume of requests while maintaining high security and speed.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
