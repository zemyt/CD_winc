## Components of the Solution:

### GitHub Actions Workflow:

- **Description:** Orchestrates automated testing and deployment tasks upon code push to the main branch.
- **Relation to other components:** Central automation tool integrating various tasks: code checkout, Python environment setup, dependency installation, testing using pytest, and secure deployment via SSH.

### Python and Testing Environment Setup:

- **Description:** Configures the Python environment, installs Flask, and sets up pytest for automated testing.
- **Relation to other components:** Facilitates execution of Flask-based tests through pytest, ensuring code functionality before deployment.

### SSH Deployment Script:

- **Description:** Uses SSH key authentication to securely connect to the deployment server, pull code changes from the main branch, and restart the service.
- **Relation to other components:** Provides deployment mechanisms, enabling integration of code updates into the live environment.

## Encountered Problems and Solutions:

### SSH Key Implementation:

- **Problem:** Connection issues between the actions workflow and the VPS due to wrongly implemented SSH keys.
- **Solution:** Resolving connection issues by verifying and correcting the SSH key implementation. Updated GitHub secrets and addressed SSH key format errors for successful VPS connection.

### Conflicting Port Usage:

- **Problem:** Issues arising from multiple sources attempting to use the same port on the VPS simultaneously.
- **Solution:** Resolving port conflicts by identifying and terminating conflicting sources, ensuring the webapp runs on the intended port.

### Sync Inconsistency Between Git and VPS:

- **Problem:** Sync inconsistency between deployed code on the VPS and the Git repository after altering .gitignore and removing Git caches.
- **Solution:** Synchronizing Git and VPS by manual updates to the VPS, aligning both code sources.
