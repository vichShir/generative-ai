import argparse


def load_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--dataset', type=str, default='mnist', required=True)
    parser.add_argument('--model', type=str, default='vae', required=True)
    parser.add_argument('--max_epochs', type=int, default=30, required=False)
    parser.add_argument('--batch_size', type=int, default=32, required=False)
    parser.add_argument('--lr', type=float, default=1e-3, required=False)
    parser.add_argument('--latent_size', type=int, default=768, required=False)
    parser.add_argument('--save_checkpoint_path', type=str, default='./', required=True)
    parser.add_argument('--load_checkpoint_path', type=str, default='./', required=False)
    parser.add_argument('--save_training_loss_per_epoch', type=int, default=1, required=False)
    parser.add_argument('--save_every', type=int, default=5, required=False)
    parser.add_argument('--validate_every', type=int, default=5, required=False)
    parser.add_argument('--seed', type=int, default=0, required=False)
    
    args = parser.parse_args()
    return args