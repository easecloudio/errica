"""
Advanced usage example showing multi-channel configuration and custom routing
"""

import os
from easecloud_errica import (
    create_monitor, ErrorMonitorConfig, task_monitor, batch_monitor, 
    log_error, send_alert, health_check, set_global_manager
)

def create_custom_config():
    """Create a custom configuration for demonstration"""
    
    # Start with environment-based config
    from easecloud_errica import create_config_from_env
    config = create_config_from_env()
    
    # Customize routing rules
    config.set_config("routing.level_routing.CRITICAL", ["telegram", "slack", "console"])
    config.set_config("routing.level_routing.ERROR", ["telegram", "console"]) 
    config.set_config("routing.level_routing.WARNING", ["slack", "console"])
    config.set_config("routing.level_routing.INFO", ["console"])
    
    # Enable console with custom formatting
    config.set_config("channels.console.enabled", True)
    config.set_config("channels.console.use_colors", True)
    config.set_config("channels.console.show_detailed_exceptions", True)
    
    # Configure Slack if webhook URL is available
    slack_webhook = os.getenv("SLACK_WEBHOOK_URL")
    if slack_webhook:
        config.set_config("channels.slack.enabled", True)
        config.set_config("channels.slack.webhook_url", slack_webhook)
        config.set_config("channels.slack.channel", "#alerts")
        config.set_config("channels.slack.username", "Error Monitor Bot")
        config.set_config("channels.slack.thread_errors", True)
    
    # Configure webhook if URL is available  
    webhook_url = os.getenv("WEBHOOK_URL")
    if webhook_url:
        config.set_config("channels.webhook.enabled", True)
        config.set_config("channels.webhook.url", webhook_url)
        config.set_config("channels.webhook.method", "POST")
        config.set_config("channels.webhook.payload_format", "json")
    
    return config


def demonstrate_task_monitoring(manager):
    """Demonstrate task and batch monitoring"""
    print("\n🔄 Demonstrating task monitoring...")
    
    # Simple task monitoring
    with task_monitor("user_sync", category="data_sync"):
        print("  Syncing users...")
        import time
        time.sleep(0.5)
        
        # Simulate an error in the task
        try:
            if True:  # Simulate error condition
                raise ValueError("User sync failed due to invalid data")
        except Exception as e:
            log_error("Error during user sync", e, {
                "users_processed": 45,
                "users_failed": 3,
                "sync_type": "incremental"
            })
            raise
    
    # Batch processing monitoring
    with batch_monitor("email_batch", category="notifications", batch_size=100):
        print("  Processing email batch...")
        
        for i in range(3):
            # Simulate batch item processing
            print(f"    Processing batch item {i+1}")
            time.sleep(0.2)
            
            if i == 1:  # Simulate an error on second item
                try:
                    raise ConnectionError("SMTP server unavailable")
                except Exception as e:
                    log_error("Email delivery failed", e, {
                        "batch_id": "batch_001",
                        "item_index": i,
                        "email_type": "newsletter"
                    })


def demonstrate_custom_channels(manager):
    """Demonstrate sending to specific channels"""
    print("\n📡 Demonstrating custom channel routing...")
    
    # Send to specific channels
    send_alert("This goes only to console", "INFO", channels=["console"])
    
    # Send critical alert to all high-priority channels
    send_alert("Critical system alert", "CRITICAL", {
        "system": "payment_processor",
        "error_code": "PP001",
        "impact": "high"
    })
    
    # Send different severity levels to see routing
    send_alert("Debug information", "DEBUG", {"debug_flag": True})
    send_alert("Warning message", "WARNING", {"warning_type": "performance"})
    send_alert("Error occurred", "ERROR", {"error_type": "validation"})


def demonstrate_health_checks(manager):
    """Demonstrate health checking"""
    print("\n🏥 Running health checks...")
    
    results = health_check()
    
    for channel, result in results.items():
        if isinstance(result, str):
            # Handle error case where result is just a string
            print(f"  ❌ {channel}: {result}")
        else:
            # Handle normal ChannelResult case
            status = "✅" if result.success else "❌"
            print(f"  {status} {channel}: {result.message}")


def demonstrate_statistics(manager):
    """Show monitoring statistics"""
    print("\n📊 Monitoring Statistics:")
    
    from easecloud_errica import get_monitoring_stats
    stats = get_monitoring_stats()
    
    # Print channel manager stats
    if "channel_manager" in stats:
        cm_stats = stats["channel_manager"]
        print(f"  📡 Active channels: {cm_stats.get('enabled_channels', [])}")
        print(f"  📝 Messages sent: {cm_stats.get('messages_sent', 0)}")
        print(f"  🚨 Errors sent: {cm_stats.get('errors_sent', 0)}")
        print(f"  ❌ Failed sends: {cm_stats.get('failed_sends', 0)}")
    
    # Print error handler stats
    if "error_handler" in stats:
        eh_stats = stats["error_handler"]
        print(f"  🛡️ Global handler enabled: {eh_stats.get('enabled', False)}")
        print(f"  📊 Total errors captured: {eh_stats.get('error_count', 0)}")


def main():
    """Advanced usage demonstration"""
    print("🚀 Starting Error Monitor advanced usage example")
    
    # Create custom configuration
    config = create_custom_config()
    
    # Validate configuration
    errors = config.validate_config()
    if errors:
        print("⚠️ Configuration warnings:")
        for channel, channel_errors in errors.items():
            for error in channel_errors:
                print(f"  - {channel}: {error}")
    
    # Create monitor with custom config
    try:
        manager, handler = create_monitor(config)
        
        # Set up global monitoring
        set_global_manager(manager)
        
        print("✅ Advanced error monitoring initialized")
        print(f"   📡 Enabled channels: {', '.join(manager.enabled_channels)}")
    except Exception as e:
        print(f"❌ Failed to initialize monitoring: {e}")
        return
    
    # Demonstrate various features
    try:
        demonstrate_task_monitoring(manager)
    except Exception:
        pass  # Expected to fail in demo
    
    demonstrate_custom_channels(manager)
    demonstrate_health_checks(manager)
    demonstrate_statistics(manager)
    
    # Test monitoring functionality
    from easecloud_errica import test_monitoring
    test_result = test_monitoring()
    print(f"\n🧪 Monitoring test result: {'✅ Passed' if test_result else '❌ Failed'}")
    
    print("\n✅ Advanced usage example completed")


if __name__ == "__main__":
    main()