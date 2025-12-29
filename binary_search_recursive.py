"""
Binary Search - Implementasi Rekursif
Untuk pencarian ID barang di gudang

Kompleksitas Waktu: O(log n)
Kompleksitas Ruang: O(log n) - karena call stack
"""

import time

def binary_search_recursive(arr, target, left=None, right=None, iterations=0, start_time=None):
    """
    Mencari ID barang menggunakan Binary Search (Rekursif)
    
    Args:
        arr: List ID barang yang sudah terurut
        target: ID barang yang dicari
        left: Index kiri (untuk rekursi)
        right: Index kanan (untuk rekursi)
        iterations: Jumlah iterasi (untuk tracking)
        start_time: Waktu mulai (untuk tracking)
    
    Returns:
        tuple: (index, iterations, time_elapsed)
    """
    # Inisialisasi pada pemanggilan pertama
    if left is None:
        left = 0
    if right is None:
        right = len(arr) - 1
    if start_time is None:
        start_time = time.perf_counter()
    
    iterations += 1
    
    # Base case: element tidak ditemukan
    if left > right:
        end_time = time.perf_counter()
        time_elapsed = (end_time - start_time) * 1000
        return (-1, iterations, time_elapsed)
    
    # Hitung middle index
    mid = (left + right) // 2
    
    # Base case: element ditemukan
    if arr[mid] == target:
        end_time = time.perf_counter()
        time_elapsed = (end_time - start_time) * 1000
        return (mid, iterations, time_elapsed)
    
    # Recursive case: cari di sebelah kiri
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, left, mid - 1, iterations, start_time)
    
    # Recursive case: cari di sebelah kanan
    else:
        return binary_search_recursive(arr, target, mid + 1, right, iterations, start_time)


def demo_recursive():
    """Demo penggunaan Binary Search Rekursif"""
    # Data ID barang di gudang (terurut)
    warehouse_items = [101, 205, 310, 415, 520, 625, 730, 835, 940, 1045,
                       1150, 1255, 1360, 1465, 1570, 1675, 1780, 1885, 1990, 2095]
    
    print("="*60)
    print("BINARY SEARCH - IMPLEMENTASI REKURSIF")
    print("="*60)
    print(f"Total barang di gudang: {len(warehouse_items)}")
    print(f"ID Barang: {warehouse_items}")
    print()
    
    # Test Case 1: Barang ditemukan
    target_id = 1255
    print(f"Mencari ID Barang: {target_id}")
    index, iterations, time_ms = binary_search_recursive(warehouse_items, target_id)
    
    if index != -1:
        print(f"✓ Barang DITEMUKAN di index: {index}")
        print(f"  Jumlah rekursi: {iterations}")
        print(f"  Waktu eksekusi: {time_ms:.6f} ms")
    else:
        print(f"✗ Barang TIDAK DITEMUKAN")
    
    print()
    
    # Test Case 2: Barang tidak ditemukan
    target_id = 999
    print(f"Mencari ID Barang: {target_id}")
    index, iterations, time_ms = binary_search_recursive(warehouse_items, target_id)
    
    if index != -1:
        print(f"✓ Barang DITEMUKAN di index: {index}")
    else:
        print(f"✗ Barang TIDAK DITEMUKAN")
        print(f"  Jumlah rekursi: {iterations}")
        print(f"  Waktu eksekusi: {time_ms:.6f} ms")
    
    print("="*60)


if __name__ == "__main__":
    demo_recursive()
