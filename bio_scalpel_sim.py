python
import numpy as np

def cnot_bio_gate(target_cell_marker, operator_trigger):
    """
    Математическая модель вентиля CNOT для Био-Скальпеля.
    target_cell_marker: 1 если клетка-цель найдена, 0 если здоровая.
    operator_trigger: 1 если оператор нажал "пуск", 0 если нет.
    """
    # Состояние системы: [Био-маркер, Лазер]
    control_qubit = target_cell_marker
    target_qubit = operator_trigger
    
    # Логика CNOT: Лазер активируется (инвертируется) только если маркер = 1
    if control_qubit == 1:
        # В идеальной квантовой системе:
        laser_output = 1 if target_qubit == 1 else 0
    else:
        # Физическая блокировка на уровне вентиля:
        laser_output = 0 
        
    return laser_output

# Тест системы "Био-Скальпель"
print("--- Проверка системы Био-Скальпель V1 ---")
test_cases = [
    (0, 1, "Здоровая клетка + Нажатие курка"),
    (1, 1, "Клетка-цель + Нажатие курка"),
    (1, 0, "Клетка-цель + Курок не нажат"),
]

for marker, trigger, desc in test_cases:
    output = cnot_bio_gate(marker, trigger)
    status = "ОГОНЬ (Разрез)" if output == 1 else "БЛОКИРОВКА (Безопасно)"
    print(f"[{desc}]: Результат -> {status}")
