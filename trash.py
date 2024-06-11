# def fix_log_of_zero(value):
#     return np.where(np.abs(value) < EPSILON, EPSILON, value)

# def get_exp(value, e=False, floor=True):
#     value = np.abs(value)
#     value = np.where(value < EPSILON, EPSILON, value)
#     if e:
#         value = np.log(value)
#     else:
#         value = np.log10(value)
#     if floor:
#         return np.floor(value)
#     else:
#         return value

# def LGLP(x, N, alpha):
#     L0 = np.ones_like(x)
#     L0_p = np.zeros_like(x)
#     L1 = 1.0 + alpha - x
#     L1_p = get_exp(L1)
#     L1 /= 10**(L1_p)

#     if N == 0:
#         Ln = L0
#         Ln_p = L0_p
#     if N == 1:
#         Ln = L1
#         Ln_p = L1_p

#     for n in range(2, N+1):
#         # exponent diff
#         L10_p_diff = L1_p - L0_p
#         Ln = (((2 * n - 1 + alpha - x)) * L1 * (10**(-L10_p_diff)) - (n - 1 + alpha) * L0) / n
#         Ln_p = L0_p + get_exp(Ln)
#         L0_p, L1_p = L1_p, Ln_p
#         L0, L1 = L1, Ln

#     return get_exp(Ln, e=True, floor=False)
