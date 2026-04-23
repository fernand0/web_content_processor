# Web Content Processor

## Description
This project provides a command-line tool to process web content, extract readable text, and optionally send it via email. It handles various content types and includes features for URL skipping and logging.

## Installation

To set up the project, follow these steps:

1.  **Clone the repository:**

    ```bash
    git clone <repository_url>
    cd web_content_processor
    ```

2.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the web content processor, use the `WebContentProcessor.py` script with the desired URL and processing mode. You can also specify sender and recipient email addresses for notifications and a configuration file for social media targets.

```bash
python web_content_processor/WebContentProcessor.py <URL> [PROCESSING_MODE] [--from-email YOUR_EMAIL] [--to-email RECIPIENT_EMAIL] [--config CONFIG_FILE]
```

**Arguments:**

*   `<URL>`: The URL of the web content to process.
*   `[PROCESSING_MODE]`: Optional. Specifies how the content should be processed. Possible values:
    *   `-txt`: Process as plain text.
    *   `-rea`: Process as readable text and mail.
    *   `-reau`: Process as readable text and mail (unconditional).
*   `--from-email YOUR_EMAIL`: Optional. The email address to use as the sender for notifications.
*   `--to-email RECIPIENT_EMAIL`: Optional. The email address to send notifications to.
*   `--config CONFIG_FILE`: Optional. Path to a JSON configuration file (default: `config.json`).

**Examples:**

*   **Process a URL and send as readable text to an email:**

    ```bash
    python web_content_processor/WebContentProcessor.py https://github.com/fernand0/web_content_processor -rea --from-email sender@example.com --to-email receiver@example.com
    ```

*   **Process a URL using a custom configuration file:**

    ```bash
    python web_content_processor/WebContentProcessor.py https://www.example.com/article -rea --config my_config.json
    ```

## Configuration

Social media targets and other settings can be configured in a JSON file. By default, the script looks for `config.json` in the current directory.

**Example `config.json`:**

```json
{
    "social_media_targets": {
        "slack": "http://fernand0-errbot.slack.com/",
        "instapaper": "fernand0kobo",
        "smtp": "ftricas@unizar.es"
    }
}
```

## Features

*   **Web Content Extraction**: Extracts readable text from web pages.
*   **URL Skipping**: Skips processing for predefined domains (e.g., YouTube, Vimeo).
*   **URL Logging**: Logs processed URLs to prevent duplication.
*   **Email Notifications**: Sends processed content via email based on processing mode.
*   **Error Handling**: Automatically sends an email notification to the recipient email address if a download error occurs, including the problematic URL and an error message.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## License

This project is licensed under the MIT License - see the LICENSE file for details. (Note: A LICENSE file is not included in this project structure. You may want to create one.)
