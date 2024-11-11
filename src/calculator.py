def add(n1, n2):
    """두 숫자를 더합니다."""
    return n1 + n2

def subtract(n1, n2):
    """첫 번째 숫자에서 두 번째 숫자를 뺍니다."""
    return n1 - n2

def multiply(n1, n2):
    """두 숫자를 곱합니다."""
    return n1 * n2

def divide(n1, n2):
    """첫 번째 숫자를 두 번째 숫자로 나눕니다.
    
    Args:
        n1: 나눠질 숫자
        n2: 나누는 숫자 (0이 아니어야 함)
    
    Raises:
        ValueError: n2가 0일 경우
    """
    if n2 == 0:
        raise ValueError("0으로 나눌 수 없습니다")
    return n1 / n2