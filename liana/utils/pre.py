import numpy as np
from scipy.sparse import csr_matrix


# Function to assert if elements are covered at a decent proportion
def _check_if_covered(
        subset,
        superset,
        subset_name="features",
        superset_name="resource",
        prop_missing_allowed=99,
        verbose=False):
    """Assert `np.all(np.isin(subset, superset))` with a more readable error
    message """
    subset = np.asarray(subset)
    is_missing = ~np.isin(subset, superset)
    prop_missing = np.sum(is_missing) / len(subset)
    x_missing = ",".join([x for x in subset[is_missing]])

    if prop_missing > prop_missing_allowed:
        msg = (
            f"Allowed proportion ({prop_missing_allowed}) of missing "
            f"{subset_name} elements exceeded ({prop_missing:.2f}). "
        )
        raise ValueError(msg + f"{x_missing} missing from {superset_name}")
    if verbose: f"{x_missing} missing from {superset_name}"


# Helper Function to check if the matrix is in the correct format
def _check_mat(X, verbose=False):
    # convert to sparse csr matrix
    if not isinstance(X, csr_matrix):
        if verbose:
            print("Converting mat to CSR format")
        X = csr_matrix(X).copy()

    # Check for empty features
    msk_features = np.sum(X != 0, axis=0).A1 == 0
    n_empty_features = np.sum(msk_features)
    if n_empty_features > 0:
        if verbose:
            print("{0} features of mat are empty, they will be removed.".format(
                n_empty_features))
        X = X[:, ~msk_features]

    # Check for empty samples
    msk_samples = np.sum(X != 0, axis=1).A1 == 0
    n_empty_samples = np.sum(msk_samples)
    if n_empty_samples > 0:
        if verbose:
            print("{0} samples of mat are empty, they will be removed.".format(
                n_empty_samples))
        X = X[:, ~msk_features]

    # Check for non finite values
    if np.any(~np.isfinite(X.data)):
        raise ValueError(
            """mat contains non finite values (nan or inf), please set them 
            to 0 or remove them.""")

    return X