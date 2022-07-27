## Error for 3_Linear

Input contains infinity or a value too large for dtype('float64').
Traceback (most recent call last):
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/base_automl.py", line 1087, in _fit
    trained = self.train_model(params)
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/base_automl.py", line 372, in train_model
    mf.train(results_path, model_subpath)
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/model_framework.py", line 249, in train
    self.callbacks.on_iteration_end(
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/callbacks/callback_list.py", line 23, in on_iteration_end
    cb.on_iteration_end(logs, predictions)
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/callbacks/early_stopping.py", line 103, in on_iteration_end
    validation_loss = self.metric(
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/utils/metric.py", line 408, in __call__
    return self.metric(y_true, y_predicted, sample_weight=sample_weight)
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/supervised/utils/metric.py", line 30, in rmse
    val = mean_squared_error(y_true, y_predicted, sample_weight=sample_weight)
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/sklearn/metrics/_regression.py", line 442, in mean_squared_error
    y_type, y_true, y_pred, multioutput = _check_reg_targets(
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/sklearn/metrics/_regression.py", line 102, in _check_reg_targets
    y_pred = check_array(y_pred, ensure_2d=False, dtype=dtype)
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/sklearn/utils/validation.py", line 899, in check_array
    _assert_all_finite(
  File "/Users/rebeccanapolitano/.conda/envs/hurricanes-manual/lib/python3.10/site-packages/sklearn/utils/validation.py", line 146, in _assert_all_finite
    raise ValueError(msg_err)
ValueError: Input contains infinity or a value too large for dtype('float64').


Please set a GitHub issue with above error message at: https://github.com/mljar/mljar-supervised/issues/new

