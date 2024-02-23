config_etth1_uni = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.012, 'mask_mode': 'mask_last',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.3,
                    'reg_weight': 0.003, 'regular_weight': 0, 'dropout': 0.1,
                    'augdropout': 0.1, 'hidden_dims': 64, 'max_train_length': 257,
                    'depth': 10, 'aug_depth': 1, 'gamma_zeta': 0.05, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': True, 'epochs': 100}

config_etth1 = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.012, 'mask_mode': 'mask_last',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.3,
                    'reg_weight': 0.2, 'regular_weight': 0, 'dropout': 0.1,
                    'augdropout': 0.1, 'hidden_dims': 128, 'max_train_length': 257,
                    'depth': 10, 'aug_depth': 1, 'gamma_zeta': 0.05, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': True, 'epochs': 35}




config_etth2_uni = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'continuous',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0, 'dropout': 0.3,
                    'augdropout': 0.2, 'hidden_dims': 128, 'max_train_length': 512,
                    'depth': 9, 'aug_depth': 2, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 80}

# todo: to be updated
config_etth2 = {'batch_size': 32, 'lr': 0.9e-05, 'meta_lr': 0.008, 'mask_mode': 'binomial',
                    'augmask_mode': 'continuous', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.2, 'regular_weight': 0.0, 'dropout': 0.3,
                    'augdropout': 0.1, 'hidden_dims': 128, 'max_train_length': 256,
                    'depth': 9, 'aug_depth': 2, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': True, 'epochs': 200}




config_ettm1_uni = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'continuous',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0, 'dropout': 0.2,
                    'augdropout': 0.2, 'hidden_dims': 128, 'max_train_length': 512,
                    'depth': 9, 'aug_depth': 1, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 190}

# todo: to be updated
config_ettm1 = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'continuous',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0, 'dropout': 0.2,
                    'augdropout': 0.2, 'hidden_dims': 128, 'max_train_length': 512,
                    'depth': 9, 'aug_depth': 1, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 300}


config_elec_uni = {'batch_size': 64, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'continuous',
                    'augmask_mode': 'binomial', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0, 'dropout': 0.3,
                    'augdropout': 0.2, 'hidden_dims': 128, 'max_train_length': 257,
                    'depth': 9, 'aug_depth': 2, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 110}

# todo: to be updated
config_elec = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'continuous',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0, 'dropout': 0.3,
                    'augdropout': 0.2, 'hidden_dims': 128, 'max_train_length': 257,
                    'depth': 9, 'aug_depth': 2, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 200}


# todo: to be updated
config_WTH_uni = {'batch_size': 64, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'mask_last',
                    'augmask_mode': 'continuous', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0.1, 'dropout': 0.1,
                    'augdropout': 0.1, 'hidden_dims': 128, 'max_train_length': 256,
                    'depth': 7, 'aug_depth': 1, 'gamma_zeta': 0.5, 'aug_dim': 64,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 480}


# todo: to be updated
config_WTH = {'batch_size': 32, 'lr': 1e-05, 'meta_lr': 0.01, 'mask_mode': 'continuous',
                    'augmask_mode': 'mask_last', 'bias_init': 0.90, 'local_weight': 0.1,
                    'reg_weight': 0.1, 'regular_weight': 0, 'dropout': 0.3,
                    'augdropout': 0.2, 'hidden_dims': 128, 'max_train_length': 512,
                    'depth': 9, 'aug_depth': 2, 'gamma_zeta': 0.02, 'aug_dim': 16,'seed':42,
                    'ratio_step': 1, 'gumbel_bias': 0.05, 'hard_mask': False, 'epochs': 100}



def merge_parameter(base_params, override_params):
    """
    Update the parameters in ``base_params`` with ``override_params``.
    Can be useful to override parsed command line arguments.

    Parameters
    ----------
    base_params : namespace or dict
        Base parameters. A key-value mapping.
    override_params : dict or None
        Parameters to override. Usually the parameters got from ``get_next_parameters()``.
        When it is none, nothing will happen.

    Returns
    -------
    namespace or dict
        The updated ``base_params``. Note that ``base_params`` will be updated inplace. The return value is
        only for convenience.
    """
    if override_params is None:
        return base_params
    is_dict = isinstance(base_params, dict)
    for k, v in override_params.items():
        if is_dict:
            if k not in base_params:
                raise ValueError('Key \'%s\' not found in base parameters.' % k)
            v = _ensure_compatible_type(k, base_params[k], v)
            base_params[k] = v
        else:
            if not hasattr(base_params, k):
                raise ValueError('Key \'%s\' not found in base parameters.' % k)
            v = _ensure_compatible_type(k, getattr(base_params, k), v)
            setattr(base_params, k, v)
    return base_params

def _ensure_compatible_type(key, base, override):
    if base is None:
        return override
    if isinstance(override, type(base)):
        return override
    if isinstance(base, float) and isinstance(override, int):
        return float(override)
    base_type = type(base).__name__
    override_type = type(override).__name__
    raise ValueError(f'Expected "{key}" in override parameters to have type {base_type}, but found {override_type}')

def merege_config(config, dataset, univar = True):
    config_out = config
    if dataset == "ETTh1":
        if univar :
            config_out = merge_parameter(config, config_etth1_uni)
        else:
            config_out = merge_parameter(config, config_etth1)
    elif dataset == "ETTh2":
        if univar :
            config_out = merge_parameter(config, config_etth2_uni)
        else:
            config_out = merge_parameter(config, config_etth2)
    elif dataset == "ETTm1":
        if univar :
            config_out = merge_parameter(config, config_ettm1_uni)
        else:
            config_out = merge_parameter(config, config_ettm1)
    elif dataset == "electricity":
        if univar :
            config_out = merge_parameter(config, config_elec_uni)
        else:
            config_out = merge_parameter(config, config_elec)
    elif dataset == "WTH":
        if univar :
            config_out = merge_parameter(config, config_WTH_uni)
        else:
            config_out = merge_parameter(config, config_WTH)
    else:
        print("not pre-config for current dataset")

    return config_out

