import argparse
from dab_app.shared.utils import get_config


def main():
    parser = argparse.ArgumentParser(description="ML Training Job")
    parser.add_argument('--env', required=True, help='Environment name (dev/staging/prod)')
    parser.add_argument('--model_type', default='xgboost', help='ML model type')
    parser.add_argument('--max_epochs', type=int, default=100, help='Maximum training epochs')
    
    args = parser.parse_args()
    
    print(f"Starting ML training job in {args.env} environment")
    print(f"Model type: {args.model_type}")
    print(f"Max epochs: {args.max_epochs}")
    
    config = get_config(args.env)
    print(f"Config loaded: {config}")
    
    # Your ML training logic here
    print("ML training completed successfully")


if __name__ == "__main__":
    main()