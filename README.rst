Welcome to Bluepass!!
=====================

Bluepass is a secure password manager with peer-to-peer sync built in. Currently it is an early beta version and needs to be installed from source.
A brief description of what this project does and who it's for.

Generic Installation Instructions
=================================

To install **Bluepass**, follow the instructions below. Specific steps for **Ubuntu** and **Fedora** are provided further down. Bluepass is designed to work on most recent **Linux distributions**, and while it can run on **macOS** and **Windows**, the **peer-to-peer sync** feature is not yet available on these platforms.

Step-by-Step Guide
-------------------

1. **Check Python Version:**
   - Ensure you have a supported version of Python installed. Bluepass works best with **Python 3.3**, though versions **2.7** and **2.6** are also supported.

2. **Set Up Python Development Environment:**
   - You'll need to compile and install **C extensions** for Python. This requires:
     - **Python development files**
     - A **C compiler**
     - `make`
     - `pip`
   - Additionally, you’ll need **git** to clone the Bluepass source code from GitHub.

3. **Install Required Dependencies:**
   - Make sure the following dependencies are installed:
     - **PyQt4**
     - **libffi** (with development files)
     - **OpenSSL** (with development files)

4. **Optional: Use Virtual Environment (Recommended):**
   - If you prefer to install Bluepass within a **virtual environment**, set one up and activate it:

        python3 -m venv bluepass-env
        source bluepass-env/bin/activate

5. **Clone the Source Code:**
   - Clone the Bluepass source from **GitHub**:

        git clone https://github.com/geertj/bluepass

6. **Install Python Packages:**
   - Inside the **Bluepass** directory, install the required Python packages:

        pip install -r requirements.txt

7. **Install Bluepass:**
   - Finally, install Bluepass by running:

        python setup.py install

Installing on Ubuntu and Fedora
===============================

For **Ubuntu 13.04** and later, and **Fedora 19** and later, **Python 3.3** is available through the distribution's package manager. It is recommended to use **Python 3** for running Bluepass on these platforms.

Step 1: Install Dependencies
-------------------------------

Both **Ubuntu** and **Fedora** provide most of the required dependencies, except for **Gruvi**. You can install the necessary dependencies using the following commands:

On Ubuntu:

   sudo apt-get -y install gcc make python3-dev python3-pyqt4 python3-pip \
       libssl-dev libffi-dev git curl

On Fedora:

   sudo yum -y install gcc make python3-devel python3-PyQt4 python3-pip \
       openssl-devel libffi-devel git curl

Then run the following commands to install Bluepass from GitHub into a virtual environment.



   - pyvenv-3.3 --system-site-packages bluepass-dev
   - source bluepass-dev/bin/activate
   - curl -O https://pypi.python.org/packages/source/p/pip/pip-1.4.1.tar.gz
   - tar xvfz pip-1.4.1.tar.gz
   - pushd pip-1.4.1
   - python setup.py install
   - popd
   - git clone https://github.com/geertj/bluepass
   - pushd bluepass
   - pip install -r requirements.txt
   - python setup.py install

To run bluepass, use:

   bluepass

On previous versions of Ubuntu and Fedora, use the generic installation instructions.

Features
========

- **Secure Password Management**: Store and manage your passwords securely with state-of-the-art encryption techniques.
- **Peer-to-Peer Synchronization**: Sync your password database across multiple devices without relying on third-party cloud services, ensuring maximum privacy and control.
- **Open Source**: Contribute to and modify the source code as per your requirements, fostering a community-driven development approach.
- **Local Storage**: Keep your passwords stored locally on your device, enhancing security and reducing dependency on external services.

Contributing
============

We welcome contributions from the community! If you're interested in helping improve Bluepass, please follow these guidelines:

How to Contribute
-----------------

1. **Fork the Repository**: Start by forking the `Bluepass GitHub repository <https://github.com/geertj/bluepass>` to your own account.

2. **Clone Your Fork**: Clone your forked repository to your local machine:

      git clone https://github.com/geertj/bluepass.git

3. **Create a New Branch**: Create a new branch for your feature or bug fix:

      git checkout -b feature/your-feature-name

4. **Make Your Changes**: Implement your feature, fix the bug, or improve the documentation as needed.

5. **Write Tests**: If applicable, write tests for your changes to ensure everything works as expected.

6. **Commit Your Changes**: Commit your changes with a clear and descriptive commit message:

      git commit -m "Add feature: Your feature description"

7. **Push to Your Fork**: Push your changes back to your forked repository:

      git push origin feature/your-feature-name

8. **Open a Pull Request**: Navigate to the original repository and open a pull request. Provide a detailed description of your changes, and reference any relevant issues.

Guidelines
----------

- **Code Style**: Follow the project's code style and conventions to maintain consistency.
- **Documentation**: If you add a new feature or change existing functionality, please update the documentation accordingly.
- **Issues**: If you encounter a bug or have a feature request, feel free to open an issue on the GitHub repository to discuss it with the maintainers.
