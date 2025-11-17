import torch
import numpy as np

# ------------------------------
# GRU 모델 불러오기 위한 클래스
# ------------------------------
class GRUModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.gru = nn.GRU(input_size=1, hidden_size=8, batch_first=True)
        self.fc = nn.Linear(8, 1)

    def forward(self, x):
        out, _ = self.gru(x)
        out = out[:, -1, :]
        out = self.fc(out)
        return out


# ------------------------------------------------
# 1) 내일 스트레스 지수 예측
# ------------------------------------------------
def predict_tomorrow(model, last_seq, scaler):
    """
    last_seq: 최근 7개 값 (numpy array)
    scaler: MinMaxScaler
    """
    seq_scaled = scaler.transform(last_seq.reshape(-1, 1))
    X_input = torch.tensor(seq_scaled.reshape(1, 7, 1), dtype=torch.float32)

    with torch.no_grad():
        pred_scaled = model(X_input).numpy()

    pred_value = scaler.inverse_transform(pred_scaled)[0][0]
    return float(pred_value)


# ------------------------------------------------
# 2) 7일(1주일) 스트레스 지수 예측
# ------------------------------------------------
def predict_week(model, last_seq, scaler):
    """
    last_seq: 최근 7개 값
    """
    seq = last_seq.copy()
    preds = []

    for _ in range(7):
        seq_scaled = scaler.transform(seq.reshape(-1, 1))
        X_input = torch.tensor(seq_scaled.reshape(1, 7, 1), dtype=torch.float32)

        with torch.no_grad():
            pred_scaled = model(X_input).numpy()

        pred_real = scaler.inverse_transform(pred_scaled)[0][0]
        preds.append(pred_real)

        # 새 예측값을 시퀀스에 추가하여 다음 예측에 사용
        seq = np.append(seq[1:], pred_real)

    return preds
