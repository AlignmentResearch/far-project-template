import wandb
from farconf import to_dict

from {{ cookiecutter.project_name }}.configs import RunConfig
from {{ cookiecutter.project_name }}.constants import PROJECT_NAME, WANDB_ENTITY
from {{ cookiecutter.project_name }}.utils.utils import flatten_dict


def setup_wandb(config: RunConfig) -> None:
    """Setups wandb for logging."""
    config_dict = to_dict(config)
    assert isinstance(config_dict, dict)
    wandb.init(
        config=flatten_dict(config_dict),
        project=PROJECT_NAME,
        entity=WANDB_ENTITY,
        group=config.experiment_name,
        name=config.run_name,
    )
