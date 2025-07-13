"""
Multi-channel demonstration showing different notification channels
"""

import os
import time
from easecloud_errica import (
    create_monitor, ErricaConfig, task_monitor, 
    log_error, log_info, log_warning, log_critical, send_alert, set_global_manager
)

def setup_demo_config():
    """Setup configuration for multi-channel demo"""
    config = ErricaConfig()
    
    # App configuration
    config.set_config("app.name", "Multi-Channel Demo")
    config.set_config("app.version", "1.0.0")
    config.set_config("app.environment", "demo")
    
    # Always enable console
    config.set_config("channels.console.enabled", True)
    config.set_config("channels.console.use_colors", True)
    config.set_config("channels.console.show_detailed_exceptions", True)
    
    # Enable Telegram if credentials are available
    telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")
    telegram_chat = os.getenv("TELEGRAM_CHAT_ID")
    if telegram_token and telegram_chat:
        config.set_config("channels.telegram.enabled", True)
        config.set_config("channels.telegram.bot_token", telegram_token)
        config.set_config("channels.telegram.chat_id", telegram_chat)
        print("📱 Telegram channel enabled")
    else:
        print("📱 Telegram channel disabled (no credentials)")
    
    # Enable Slack if webhook is available
    slack_webhook = os.getenv("SLACK_WEBHOOK_URL")
    if slack_webhook:
        config.set_config("channels.slack.enabled", True)
        config.set_config("channels.slack.webhook_url", slack_webhook)
        config.set_config("channels.slack.channel", "#errica-demo")
        config.set_config("channels.slack.username", "Demo Bot")
        print("💬 Slack channel enabled")
    else:
        print("💬 Slack channel disabled (no webhook URL)")
    
    # Enable webhook if URL is available
    webhook_url = os.getenv("WEBHOOK_URL")
    if webhook_url:
        config.set_config("channels.webhook.enabled", True)
        config.set_config("channels.webhook.url", webhook_url)
        config.set_config("channels.webhook.method", "POST")
        config.set_config("channels.webhook.payload_format", "json")
        print("🌐 Webhook channel enabled")
    else:
        print("🌐 Webhook channel disabled (no webhook URL)")
    
    # Configure routing for demo
    config.set_config("routing.level_routing.CRITICAL", ["telegram", "slack", "webhook", "console"])
    config.set_config("routing.level_routing.ERROR", ["telegram", "slack", "console"])
    config.set_config("routing.level_routing.WARNING", ["slack", "console"])
    config.set_config("routing.level_routing.INFO", ["console"])
    
    return config


def demo_basic_logging(manager):
    """Demonstrate basic logging to different channels"""
    print("\n📝 Demo: Basic Logging")
    
    log_info("Demo application started")
    time.sleep(1)
    
    log_info("Processing user data", {"users": 150, "processing_time": "2.3s"})
    time.sleep(1)
    
    log_warning("High memory usage detected", {
        "memory_usage": "85%",
        "threshold": "80%",
        "recommendation": "Consider scaling up"
    })
    time.sleep(1)
    
    log_error("Database connection failed", context={
        "database": "user_db",
        "host": "db.example.com",
        "port": 5432,
        "error_code": "CONNECTION_TIMEOUT"
    })
    time.sleep(1)


def demo_exception_handling(manager):
    """Demonstrate exception handling"""
    print("\n🚨 Demo: Exception Handling")
    
    # Simple exception
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        log_error("Division by zero error", e, {
            "operation": "division",
            "numerator": 10,
            "denominator": 0
        })
        time.sleep(1)
    
    # Complex exception with nested calls
    def process_data():
        def validate_data(data):
            if not data:
                raise ValueError("Data cannot be empty")
            if len(data) < 5:
                raise ValueError("Data must have at least 5 items")
            return data
        
        def transform_data(data):
            return [x * 2 for x in data]
        
        try:
            raw_data = []  # Empty data to trigger error
            validated = validate_data(raw_data)
            transformed = transform_data(validated)
            return transformed
        except ValueError as e:
            log_error("Data processing failed", e, {
                "step": "validation",
                "data_size": len(raw_data),
                "expected_min_size": 5
            })
            raise
    
    try:
        process_data()
    except ValueError:
        pass  # Already logged
    
    time.sleep(1)


def demo_task_monitoring(manager):
    """Demonstrate task monitoring"""
    print("\n⚙️ Demo: Task Monitoring")
    
    # Successful task
    with task_monitor("data_backup", category="maintenance"):
        log_info("Starting data backup process")
        time.sleep(1)
        log_info("Backup completed successfully", {"files_backed_up": 1250, "size": "2.3GB"})
    
    time.sleep(1)
    
    # Failed task
    try:
        with task_monitor("api_sync", category="integration"):
            log_info("Syncing with external API")
            time.sleep(0.5)
            
            # Simulate API failure
            raise ConnectionError("API endpoint returned 503 Service Unavailable")
    except ConnectionError:
        pass  # Error already captured by task monitor
    
    time.sleep(1)


def demo_critical_alerts(manager):
    """Demonstrate critical alerts"""
    print("\n🚨 Demo: Critical Alerts")
    
    log_critical("System disk space critically low", context={
        "disk_usage": "95%",
        "available_space": "2.1GB",
        "threshold": "90%",
        "action_required": "Immediate cleanup needed"
    })
    time.sleep(2)
    
    try:
        raise RuntimeError("Payment processor service crashed")
    except RuntimeError as e:
        log_critical("Critical service failure", e, {
            "service": "payment_processor",
            "impact": "All payments blocked",
            "priority": "P0",
            "escalation": "Required"
        })
    
    time.sleep(2)


def demo_custom_alerts(manager):
    """Demonstrate custom alerts with specific routing"""
    print("\n📢 Demo: Custom Alerts")
    
    # Send to specific channels
    send_alert("Maintenance window starting", "INFO", 
               {"start_time": "2024-01-15 02:00 UTC", "duration": "2 hours"},
               channels=["slack", "console"])
    time.sleep(1)
    
    # Send security alert
    send_alert("Suspicious login detected", "WARNING", {
        "user": "admin@example.com",
        "ip": "192.168.1.100",
        "location": "Unknown",
        "action": "Login blocked"
    })
    time.sleep(1)
    
    # Send performance alert
    send_alert("API response time degraded", "WARNING", {
        "endpoint": "/api/users",
        "avg_response_time": "2.5s",
        "threshold": "1.0s",
        "requests_affected": 150
    })
    time.sleep(1)


def demo_health_checks(manager):
    """Demonstrate health checks"""
    print("\n🏥 Demo: Health Checks")
    
    from easecloud_errica import health_check
    results = health_check()
    
    all_healthy = True
    for channel, result in results.items():
        if isinstance(result, str):
            # Handle error case where result is just a string
            print(f"  {channel}: ❌ {result}")
            all_healthy = False
        else:
            # Handle normal ChannelResult case
            status = "✅ Healthy" if result.success else f"❌ Unhealthy: {result.message}"
            print(f"  {channel}: {status}")
            if not result.success:
                all_healthy = False
    
    if all_healthy:
        log_info("All channels are healthy")
    else:
        log_warning("Some channels are unhealthy", {"unhealthy_channels": [
            ch for ch, res in results.items() if not res.success
        ]})


def main():
    """Run the multi-channel demonstration"""
    print("🚀 Starting Multi-Channel Errica Demo")
    print("=" * 50)
    
    # Setup configuration
    config = setup_demo_config()
    
    # Create monitor
    try:
        manager, handler = create_monitor(config)
        
        # Set up global monitoring
        set_global_manager(manager)
        
        enabled_channels = manager.enabled_channels
        print(f"\n✅ Monitor initialized with channels: {', '.join(enabled_channels)}")
    except Exception as e:
        print(f"❌ Failed to initialize monitor: {e}")
        return
    
    print("\n🎯 This demo will send messages to all configured channels.")
    print("   Watch your Telegram, Slack, and webhook endpoints!")
    print("\nStarting demo in 3 seconds...")
    time.sleep(3)
    
    try:
        # Run demonstrations
        demo_basic_logging(manager)
        demo_exception_handling(manager)
        demo_task_monitoring(manager)
        demo_critical_alerts(manager)
        demo_custom_alerts(manager)
        demo_health_checks(manager)
        
        # Show final statistics
        print("\n📊 Final Statistics:")
        from easecloud_errica import get_monitoring_stats
        stats = get_monitoring_stats()
        
        if "channel_manager" in stats:
            cm_stats = stats["channel_manager"]
            print(f"  Messages sent: {cm_stats.get('messages_sent', 0)}")
            print(f"  Errors sent: {cm_stats.get('errors_sent', 0)}")
            print(f"  Failed sends: {cm_stats.get('failed_sends', 0)}")
        
        log_info("Multi-channel demo completed successfully")
        print("\n✅ Demo completed! Check your configured channels for messages.")
        
    except KeyboardInterrupt:
        print("\n⏹️ Demo interrupted by user")
        log_warning("Demo stopped by user interrupt")
    except Exception as e:
        print(f"\n❌ Demo failed: {e}")
        log_error("Demo execution failed", e)
    finally:
        # Cleanup
        if manager:
            manager.shutdown()


if __name__ == "__main__":
    main()