import numpy as np

def compute_absurdity(semantic_grad, lexical_grad, proj_jacobian):
    """
    semantic_grad: градиент смысловой плотности на M (псевдо)
    lexical_grad: градиент на L
    proj_jacobian: матрица Якоби проекции
    """
    # Упрощённо: разница норм с учётом проекции
    mapped_lex = proj_jacobian @ lexical_grad
    diff = np.linalg.norm(semantic_grad)**2 - np.linalg.norm(mapped_lex)**2
    return abs(diff)

def kernel_size_estimate(dim_M, dim_L):
    return dim_M - dim_L  # предполагаем сюръективность
