import argparse
from dab_app.shared.utils import get_config


def main():
    parser = argparse.ArgumentParser(description="Data Processing Job")
    parser.add_argument('--env', required=True, help='Environment name (dev/staging/prod)')
    parser.add_argument('--batch_size', type=int, default=1000, help='Batch size for processing')
    parser.add_argument('--input_path', help='Input data path')
    
    args = parser.parse_args()
    
    print(f"Starting data processing job in {args.env} environment")
    print(f"Batch size: {args.batch_size}")
    
    config = get_config(args.env)
    print(f"Config loaded: {config}")
    
    # Your data processing logic here
    print("Data processing completed successfully")


if __name__ == "__main__":
    main()