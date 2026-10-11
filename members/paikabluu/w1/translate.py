def primes_up_to(n: int) -> list[int]:
    """
    Khác biệt so với C++:
    Thay vì dùng vòng lặp for truyền thống để lấy mảng kết quả, Python 
    cho phép dùng List Comprehension kết hợp hàm enumerate() ở cuối 
    để lọc giá trị cực kỳ ngắn gọn và mang đậm phong cách "Pythonic".
    """
    if n < 2:
        return []
        
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    return [p for p, prime in enumerate(is_prime) if prime]