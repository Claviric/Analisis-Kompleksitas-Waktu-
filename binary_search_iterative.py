"""
Binary Search - Implementasi Iteratif
Untuk pencarian ID barang di gudang

Kompleksitas Waktu: O(log n)
Kompleksitas Ruang: O(1)
"""

import time

def binary_search_iterative(arr, target):
    """
    Mencari ID barang menggunakan Binary Search (Iteratif)
    
    Args:
        arr: List ID barang yang sudah terurut
        target: ID barang yang dicari
    
    Returns:
        tuple: (index, iterations, time_elapsed)
    """
    start_time = time.perf_counter()
    
    left = 0
    right = len(arr) - 1
    iterations = 0
    
    while left <= right:
        iterations += 1
        mid = (left + right) // 2
        
        # Barang ditemukan
        if arr[mid] == target:
            end_time = time.perf_counter()
            time_elapsed = (end_time - start_time) * 1000  # Konversi ke ms
            return (mid, iterations, time_elapsed)
        
        # Target ada di sebelah kanan
        elif arr[mid] < target:
            left = mid + 1
        
        # Target ada di sebelah kiri
        else:
            right = mid - 1
    
    # Barang tidak ditemukan
    end_time = time.perf_counter()
    time_elapsed = (end_time - start_time) * 1000
    return (-1, iterations, time_elapsed)


def demo_iterative():
    """Demo penggunaan Binary Search Iteratif"""
    # Data ID barang di gudang (terurut)
    warehouse_items = [101, 205, 310, 415, 520, 625, 730, 835, 940, 1045,
                       1150, 1255, 1360, 1465, 1570, 1675, 1780, 1885, 1990, 2095]
    
    print("="*60)
    print("BINARY SEARCH - IMPLEMENTASI ITERATIF")
    print("="*60)
    print(f"Total barang di gudang: {len(warehouse_items)}")
    print(f"ID Barang: {warehouse_items}")
    print()
    
    # Test Case 1: Barang ditemukan
    target_id = 1255
    print(f"Mencari ID Barang: {target_id}")
    index, iterations, time_ms = binary_search_iterative(warehouse_items, target_id)
    
    if index != -1:
        print(f"✓ Barang DITEMUKAN di index: {index}")
        print(f"  Jumlah iterasi: {iterations}")
        print(f"  Waktu eksekusi: {time_ms:.6f} ms")
    else:
        print(f"✗ Barang TIDAK DITEMUKAN")
    
    print()
    
    # Test Case 2: Barang tidak ditemukan
    target_id = 999
    print(f"Mencari ID Barang: {target_id}")
    index, iterations, time_ms = binary_search_iterative(warehouse_items, target_id)
    
    if index != -1:
        print(f"✓ Barang DITEMUKAN di index: {index}")
    else:
        print(f"✗ Barang TIDAK DITEMUKAN")
        print(f"  Jumlah iterasi: {iterations}")
        print(f"  Waktu eksekusi: {time_ms:.6f} ms")
    
    print("="*60)


if __name__ == "__main__":
    demo_iterative()
