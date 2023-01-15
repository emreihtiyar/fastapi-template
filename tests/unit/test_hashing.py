import pytest
from src.security.hashing import HashHelper


@pytest.mark.parametrize(
    "password", 
    [
        "pass","işçöüğ","12345", 
        "$argon2id$v=19$m=65536,t=3,p=4$gTCmtPae857znrPWWisFoA$UoDDREuki2jjDZyybSGgcIdRxmqYxmMg1frErPQI2f0"
    ]
)
def test_hashing(password):
    hash_helper = HashHelper()
    hashed_password = hash_helper.hash(password)
    hashed_passwor2 = hash_helper.hash(password)
    assert hashed_password != hashed_passwor2, "Hashed passwords should be different"

@pytest.mark.parametrize(
    "password, hashed_password",
    [
        ("password", "$argon2id$v=19$m=65536,t=3,p=4$gTCmtPae857znrPWWisFoA$UoDDREuki2jjDZyybSGgcIdRxmqYxmMg1frErPQI2f0"),
        ("işçöüğ", "$argon2id$v=19$m=65536,t=3,p=4$RghBKOVcq/We836vFaL03g$jiC7bbU/Fq1MTVt7A6HzQENse3xBSwoajbxC3hVVN3k"),
        ("password", "$argon2id$v=19$m=65536,t=3,p=4$gTCmtPae857znrPWWisFoA$UoDDREuki2jjDZyybSGgcIdRxmqYxmMg1frErPQI2f0"),
    ]
)
def test_hashing_with_params(password, hashed_password):
    hash_helper = HashHelper()
    assert hash_helper.verify(password, hashed_password) is True, "Correct password should verify"

@pytest.mark.parametrize(
    "password, hashed_password",
    [
        ("password", "$argon2id$v=19$m=65536,t=3,p=4$gTCmtPae857znrPWWisFoA$UoDDREuki2jjDZyybSGgcId"),
        ("işçöüğ", "$argon2id$v=19$m=65536,t=3,p=4$RghBKOVcq/We836vFaL03g$jiC7bbU/Fq1MTVt7A6HzQENse3xBSwoajbxC3hVVN3ds"),
        ("password", "$argon2id$v=19$m=65536,t=3,p=4$gTCmtPae857znrPWWisFoA$UoDDREuki2jjDZyybSGgcIdRxmqYxmMg1frErPQ1220"),
    ]
)
def test_hashing_with_wrong_params(password, hashed_password):
    hash_helper = HashHelper()
    assert hash_helper.verify(password, hashed_password) is False, "Wrong password should not verify"