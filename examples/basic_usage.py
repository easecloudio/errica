"""
Basic usage example for the Errica package
"""

import os
from easecloud_errica import quick_setup, task_monitor, log_error, log_info, send_alert

# Set environment variables for configuration
# In production, these would be set in your environment or configuration files
os.environ["APP_NAME"] = "Example App"
os.environ["APP_VERSION"] = "0.1.0-beta"
os.environ["ENVIRONMENT"] = "development"

# Example: Enable console output (always enabled by default)
# For Telegram: Set TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID
# For Slack: Set SLACK_WEBHOOK_URL
# For Webhook: Set WEBHOOK_URL

def main():
    """Basic usage example"""
    print("🚀 Starting Errica basic usage example")
    
    # Quick setup - automatically detects configuration from environment
    try:
        manager, handler = quick_setup()
        print("✅ Errica initialized successfully")
    except Exception as e:
        print(f"❌ Failed to initialize Errica: {e}")
        return
    
    # Log some basic messages
    log_info("Application started successfully")
    log_info("This is an informational message")
    
    # Send a custom alert
    send_alert("Custom alert message", "WARNING", {"user_id": 123, "action": "login"})
    
    # Monitor a task
    with task_monitor("example_task", category="demo"):
        log_info("Executing example task")
        
        # Simulate some work
        import time
        time.sleep(1)
        
        log_info("Task work completed")
    
    # Demonstrate error handling
    try:
        # This will raise an exception
        result = 10 / 0
    except Exception as e:
        # This will be sent to configured channels with full context
        log_error("Division by zero error occurred", e, {
            "operation": "division",
            "numerator": 10,
            "denominator": 0
        })
    
    # Test critical error
    try:
        raise RuntimeError("This is a critical error simulation")
    except Exception as e:
        # Critical errors go to all configured high-priority channels
        from easecloud_errica import log_critical
        log_critical("Critical system error", e, {
            "severity": "high",
            "requires_immediate_attention": True
        })
    
    # Get monitoring statistics
    from easecloud_errica import get_monitoring_stats
    stats = get_monitoring_stats()
    print(f"📊 Monitoring stats: {stats}")
    
    log_info("Example completed successfully")
    print("✅ Basic usage example completed")


if __name__ == "__main__":
    main()