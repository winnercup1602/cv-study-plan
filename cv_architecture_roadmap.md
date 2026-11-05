# CV 핵심 개념과 모델 스터디 계획

## 1. 운영계획

**주 1회, 회당 60분(방학 중에는 주 2회)** 동안 CV의 핵심 개념과 모델을 함께 공부합니다. **개념이 필요한 이유, 구조와 수식의 의미, 실제 동작 원리를 깊이 이해하는 것**을 목표로 합니다. 배운 내용을 자신의 언어와 구조도·수식·코드로 설명하고, 연구에서 설계와 활용을 판단하는 데 연결합니다.

### 1. 세션 준비와 진행

담당자는 아래 여섯 단계에 따라 내용을 준비하고, 세션도 같은 순서로 진행합니다. 목표는 개념이 필요한 이유와 작동 원리를 이해하고, 그 효과와 한계, 연구에서의 활용까지 연결하는 것입니다.

기준 논문이 있는 주제는 해당 논문을 출발점으로 삼습니다. 그 외에는 여러 논문·교재·강의·공식 문서·코드를 참고해 설명을 구성합니다. 각 회차는 본문에 명시한 중심 모델·핵심 흐름을 우선하고, Related Work는 확장 참고 목록으로 활용합니다. 세션에서 비교할 연구는 해당 회차의 학습 범위에 맞춰 선택합니다. 각 단계를 펼쳐 세부 준비 안내를 확인할 수 있습니다.

#### 시작 점검 · **5분** (0–5분)

| 소요 시간 | 진행 구간 | 단계 | 중심 질문 | 세부 안내 |
|---|---|---|---|---|
| **5분** | 0–5분 | 이전 내용 복습 + 학습 포인트 제시 | 지난 내용과 이번 학습 목표는 무엇인가? | **이전 복습:** 지난 공유 기록의 학습 포인트·수정한 설명·남은 질문. 첫 세션은 선수 개념 점검<br>**이번 제시:** 주제·학습 포인트<br>**사전 준비:** 시작·종료에 같은 문장·항목·순서의 작성지, 설명·수식·도식 작성 공간, 인원수에 맞춰 출력 |

#### 세션 프레임워크 · **45분** (5–50분)

| 소요 시간 | 진행 구간 | 단계 | 중심 질문 | 세부 안내 |
|---|---|---|---|---|
| **5분** | 5–10분 | 1. Why · 필요성 | 왜 이 개념이 필요한가? | **문제 상황:** 해결할 문제·기존 접근의 어려움·구체적인 예<br>**필요성:** 이 개념으로 달라지는 점·기대하는 효과 |
| **5분** | 10–15분 | 2. What · 아이디어와 원리 | 문제를 해결하는 아이디어는 무엇인가? | **중심 아이디어:** 한 문장 설명·직관적인 그림<br>**개념과 가정:** 주요 용어·성립 조건<br>**주요 수식:** 기호·각 항의 의미와 아이디어의 연결 |
| **20분** | 15–35분 | 3. How · 구조와 동작 | 실제로 어떻게 작동하는가? | **동작 흐름:** 입력 → 계산·변환 → 출력, 구성요소의 역할·연결<br>**학습과 추론:** 동작 차이·target·loss·gradient·고정/갱신 파라미터(해당 시)<br>**수식·코드:** 차원·연산 위치, 작은 입력 예제의 계산 추적<br>**구조 비교:** 구성요소 제거·변경 시의 차이 |
| **5분** | 35–40분 | 4. Evidence · 근거와 비교 | 효과와 설계 이유를 무엇으로 확인하는가? | **대표 근거:** 실험·적용 사례·간단한 계산<br>**비교 흐름:** 질문 → 비교 대상·변경 요소·고정 조건 → 결과 → 해석<br>**설계 이유:** ablation·평가 지표·계산 비용(해당 시)<br>**근거 구분:** 자료에서 확인한 사실 / 직접 확인한 결과 / 자신의 해석 |
| **5분** | 40–45분 | 5. Related Work · 관련 연구와 발전 흐름 | 다른 연구에서는 어떻게 이어지고 달라졌는가? | **자료 선정:** 주제 이해에 도움이 되는 대표 자료·후속 연구, 비교는 2–3개 이내<br>**발전 흐름:** 유지·변형·대체된 원리와 구조<br>**핵심 차이:** 최근 활용 방식·접근별 차이·참고 자료 |
| **5분** | 45–50분 | 6. Limitations & Applications · 한계와 연구 활용 | 어디까지 유효하며, 우리 연구에는 어떻게 활용할 수 있는가? | **조건과 한계:** 유용한 상황·가정·실패 조건<br>**적용 제약:** 데이터·학습 조건·계산 비용<br>**연구 연결:** 활용 지점·추가 확인 질문·후속 실험<br>**근거 구분:** 확인된 결과 / 검증 전 활용 아이디어 |

#### 학습 정리 · **10분** (50–60분)

| 소요 시간 | 진행 구간 | 단계 | 중심 질문 | 세부 안내 |
|---|---|---|---|---|
| **10분** | 50–60분 | 학습 포인트 확인·공유 기록 | 학습 포인트를 자신의 언어로 설명할 수 있는가? | **각자 작성 · 5분:** 자료·다른 사람의 답을 덮고 모든 항목에 설명·수식·도식 작성, 막힌 부분·남은 질문 표시<br>**함께 확인·기록 · 5분:** 답의 주요 차이·오해 확인, 학습 포인트별 수정한 설명·남은 질문·근거 위치 기록. 다음 복습의 기준<br>**세션 후 보완:** 공유 기록의 문장·그림·수식·근거 정리 |

### 2. 학습 포인트 확인

**시작에 안내한 학습 포인트를 같은 문장·항목·순서로 다시 확인합니다.**

1. **각자 작성 · 5분.** 자료나 다른 사람의 답을 보지 않고, 인쇄된 작성지의 모든 항목에 설명·수식·도식으로 답합니다. 막힌 부분도 표시합니다.
2. **함께 확인·기록 · 5분.** 답의 주요 차이와 오해를 확인하고, 수정한 설명·남은 질문·근거 위치를 공유 기록의 초안으로 남깁니다. 세션 후 보완해 다음 복습의 기준으로 사용합니다.

작성지에는 항목별로 **내 설명·수식·도식 / 막힌 부분·남은 질문** 공간을 둡니다.

<!-- point-example:transformer label:Transformer -->

주제: **토큰 사이의 정보 교환과 encoder–decoder의 작동 원리**

- [ ] **1. 왜 토큰 사이에 정보를 주고받아야 할까요?** “고양이가 우유를 마신다”에서 각 토큰을 따로 처리하는 경우와 문맥을 함께 반영하는 경우를 비교하고, self-attention을 사용하는 이유를 설명해 보세요.
- [ ] **2. 다른 토큰의 정보가 내 표현에 어떻게 섞이나요?** 한 토큰의 표현을 갱신하는 과정을 수식과 그림으로 나타내고, Q·K·V·softmax와 여러 head의 역할을 설명해 보세요.
- [ ] **3. 입력 문장이 출력 문장으로 바뀌는 구조는 어떻게 작동하나요?** encoder와 decoder의 정보 흐름을 그리고, positional encoding·self-attention·cross-attention·FFN이 각각 어떤 역할을 하는지 짚어 보세요.
- [ ] **4. 왜 학습은 병렬로 계산하고 생성은 순차적으로 하나요?** decoder 입력과 정답의 관계, causal mask, 생성 시 이용할 수 있는 정보를 기준으로 설명해 보세요.

참고자료: [Attention Is All You Need — 원문](https://arxiv.org/pdf/1706.03762), §3.1–3.5, Figure 1·2 및 Eq. (1). 문장은 원리 설명을 위한 예시입니다.
<!-- /point-example -->

<!-- /운영계획 -->

---

## 2. 학습 항목

신경망 기초부터 생성 모델까지 0–3장의 학습 항목을 정리합니다. 각 모델의 구조·수식·학습·구현을 함께 살펴보며, 원리가 밀접하게 연결된 후속 모델은 주요 변화를 비교합니다.


### 개념 유형 구분

학습 항목 옆의 유형은 해당 항목의 성격과 세션에서 중점적으로 다루는 역할을 나타냅니다. 둘 이상의 관점으로 다루면 **모델 · 학습 방법**처럼 함께 표기합니다.

| 유형 | 의미 | 예시 |
|---|---|---|
| 기초 개념 | 텐서 표현과 layer의 동작, 초기화 등 모델 이해의 바탕 | Tensor / Linear / MLP, Activation / Initialization |
| 기초 연산 | 모델을 구성하는 기본 계산과 변환 | Attention, Normalization |
| 학습 원리 | 오차를 정의하고 gradient를 계산하는 원리 | Loss / Backpropagation |
| 학습 방법 | 학습 신호·목표·업데이트·전이 방식을 정하는 방법 | Optimization, Regularization, SimCLR, DINO, MAE |
| 모델 구조 | 여러 모델에서 활용하는 블록 구성과 정보 흐름 | Transformer |
| 모델 | 구조와 학습 목표를 특정 작업에 맞게 구성한 전체 | ViT, CLIP, DETR, DPT, SAM |
| 구성 요소 | 모델 안에서 위치 정보 전달 등 특정 역할을 맡는 구조 | Positional Encoding Variants |
| 구현 기법 | 계산 목표를 유지하며 연산·메모리 사용·실행 흐름을 효율화하는 기법 | FlashAttention, KV cache |
| 적응 방법 | 사전학습 모델을 새로운 작업이나 데이터 분포에 맞게 조정하는 기법 | LoRA |
| 분석 방법 | 학습 상태·데이터·모델의 표현과 특성을 관찰하고 평가하는 방법 | 모델 진단, PCA, t-SNE, UMAP |
| 생성 모델 | 데이터 분포를 학습해 새 샘플을 만드는 모델 계열과 시스템 | VAE, GAN, DDPM, Latent Diffusion |
| 생성 방법 | 생성 경로·sampling 절차 또는 이를 위한 학습 목표를 정의하는 방법 | DDIM, Flow Matching, Rectified Flow |

**Backbone·Denoiser·조건 제어**는 모델의 역할을 덧붙이는 표기입니다. 각각 feature 추출, 생성 과정의 상태 갱신에 필요한 값 예측, 조건 입력 반영을 뜻합니다. 예를 들어 ViT는 **모델 · Backbone**, DiT는 **모델 · Denoiser**, ControlNet은 **모델 · 조건 제어**로 표시합니다.

유형과 함께 구조·학습 목표·데이터·학습과 추론의 흐름을 살펴보고, 설계의 효과와 한계를 설명할 수 있는 것을 목표로 합니다.

---

### 0. 신경망 기초와 실험·분석 도구

#### 학습 목표

Dataset에서 batch를 만들고 작은 신경망의 입력·예측·loss·gradient·파라미터 갱신을 연결해 설명한다. 학습 안정성과 일반화의 기본 원리를 구분하고, 데이터 분할·비교 실험·학습 곡선으로 결과를 판단한다. 층별 activation·weight·gradient 통계와 유사도 검색으로 모델 내부와 학습한 표현을 분석한다. PCA·t-SNE·UMAP으로 feature를 직접 시각화하고, 설정에 따른 변화와 저차원 배치의 해석 한계를 설명한다.

#### 학습 내용

#### 0-A. Neural Network Basics

##### 1회차 · 2026.11.05 (목) · 발표자: 김재순 · 신경망의 표현과 비선형성

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Tensor / Linear / MLP | 기초 개념 | 필수 | **포함 개념:** Tensor shape · Batch / Channel / Spatial / Token axes · Reshape / Transpose · Matrix multiplication · Broadcasting · Linear layer · Parameter count · MLP<br>**텐서와 연산:** 작은 입력에서 축의 의미, reshape·transpose 전후 shape, 행렬 곱·broadcasting의 조건 확인<br>**Linear와 MLP:** 가중치·bias·파라미터 수, batch 내 가중치 공유, 입력 → 은닉 표현 → logits의 수식·코드 연결 |
| Activation / Initialization | 기초 개념 | 필수 | **포함 개념:** Nonlinearity · ReLU · GELU / SiLU · Sigmoid / Tanh · Saturation · Xavier / He initialization · Vanishing / Exploding gradients<br>**핵심 설명:** activation이 없을 때 Linear의 연속 적용이 하나의 affine 변환으로 합쳐지는 이유, ReLU의 출력·gradient와 sigmoid의 saturation 비교<br>**초기화 확인:** Xavier·He의 목적과 대표 적용 조건, 초기화 크기에 따른 층별 출력·gradient 그래프 비교<br>**비교 범위:** GELU·SiLU·tanh는 모양·특성 비교표로 확인. 함수별 상세 유도와 초기화 분산식의 증명은 제외 |

##### 2회차 · 2026.11.12 (목) · 발표자: 강근영 · DataLoader에서 파라미터 갱신까지

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DataLoader / Loss / Backpropagation | 기초 개념 · 학습 원리 | 필수 | **포함 개념:** Dataset / DataLoader · __len__ / __getitem__ · Input–Target pairs / Transforms · Batch size / Shuffle · collate_fn / Batch shape · Iteration / Epoch · Device transfer · Logits / Probability / Target · Output–Target shape / Dtype · Cross-entropy / MSE · Computational graph / Chain rule · Backpropagation / Autograd · requires_grad / detach · Gradient accumulation / Reset · zero_grad / backward / step<br>**데이터에서 batch까지:** Dataset이 한 입력·target을 반환하고 DataLoader가 샘플을 선택·결합해 batch를 만드는 흐름. 작은 이미지 예제에서 sample·batch의 shape, batch_size·shuffle, iteration·epoch를 확인. collate_fn은 샘플 결합·가변 길이 padding의 역할까지 비교<br>**예측과 오차:** batch를 device로 옮겨 모델에 입력하고 logits·확률·target을 연결. 분류 cross-entropy와 회귀 MSE의 용도, loss와 정확도의 차이를 확인. 기존의 작은 분류 예제에서 logits [B,C]·class-index target [B]의 shape와 자료형을 짚고(B: batch 크기, C: class 수), logits는 부동소수점·target은 torch.long임을 확인. CrossEntropyLoss에는 softmax 전 logits 입력<br>**역전파와 자동미분:** Backpropagation은 계산 그래프를 거꾸로 따라 chain rule로 gradient를 구하는 방법, Autograd는 연산을 기록하고 그 미분을 자동 계산하는 PyTorch 기능. 간단한 그래프의 gradient를 손으로 구한 뒤 backward 결과와 비교<br>**Gradient 경계:** 같은 작은 계산 그래프에서 requires_grad로 어떤 입력·파라미터의 gradient가 필요한지 지정하고, detach가 중간 표현의 이전 그래프 연결을 끊는 위치를 확인. 파라미터를 고정하는 것과 해당 연산을 통한 입력 쪽 gradient 전달을 끊는 것을 구분<br>**학습 루프:** batch → zero_grad → forward → loss → backward → step을 하나의 준비된 코드에서 추적. gradient 누적·초기화, 미분 계산과 optimizer의 파라미터 갱신을 구분<br>**학습 범위:** 작은 Dataset·DataLoader와 한 번의 학습 step을 직접 추적. Shape·자료형·gradient 경계는 이 회차 담당자가 준비한 기존 loss 예제·계산 그래프 안에서 확인. 데이터 로딩 성능 튜닝·분산 sampler·worker 내부 구현은 확장 학습으로 연결 |
| Optimization / LR Scheduling | 학습 방법 | 필수 | **포함 개념:** Mini-batch GD · SGD · Momentum / Adam / AdamW · Learning rate · Warmup · Cosine decay · L2 penalty / Weight decay<br>**핵심 설명:** mini-batch gradient와 SGD의 한 번 갱신을 계산, 학습률이 갱신 크기와 안정성에 미치는 영향<br>**대표 비교:** 준비된 갱신식 표로 Momentum의 누적 방향·Adam의 적응적 스케일·AdamW의 decoupled weight decay 확인. Adam에서 L2 penalty와 decoupled decay의 차이 구분<br>**비교 범위:** warmup·cosine은 학습률 곡선과 적용 위치 확인. optimizer별 전체 수식 유도·상태 변수 계산과 여러 schedule의 상세 비교는 제외 |

##### 3회차 · 2026.11.19 (목) · 발표자: 이소윤 · 학습 안정성·일반화·훈련 기법

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Normalization | 기초 연산 | 필수 | **포함 개념:** BatchNorm (BN) · LayerNorm (LN) · GroupNorm (GN) · RMSNorm · Normalization axes · Scale / Bias · Running statistics · train / eval · no_grad · Training / Evaluation modes<br>**핵심 계산:** 작은 텐서에서 BN·LN의 정규화 축과 평균·분산 계산, 학습 가능한 scale·bias의 역할<br>**학습과 추론:** 기본 BN의 batch 통계·누적 통계, LN의 입력 기반 통계와 train·eval 동작 구분<br>**동작 모드와 미분:** model.train()/eval()은 BN·dropout처럼 학습/평가에 따라 달라지는 모듈의 동작을 선택하고, no_grad()는 해당 구간의 역전파용 연산 기록을 끄는 기능. eval()만으로 gradient 계산이 꺼지지는 않으며, 이 회차의 BN·dropout 예제에서 동작 모드와 연산 기록 여부를 나누어 확인<br>**비교 범위:** GN·RMSNorm은 계산 축·batch 의존성·평균 제거 여부를 비교표로 확인. 네 방식 모두의 상세 유도·구현은 제외 |
| Regularization | 학습 방법 | 필수 | **포함 개념:** Generalization · Overfitting / Underfitting · Training / Validation gap · Dropout · Weight decay · Data augmentation · Mixup / CutMix<br>**일반화 진단:** 준비된 학습·검증 곡선에서 과적합·과소적합 구분, 성능을 판단할 때 확인할 데이터 분할과 지표<br>**대표 방법:** dropout의 mask·스케일 조정·학습/추론 차이, weight decay와 데이터 증강이 개입하는 위치·가정. 갱신식은 2회차 Optimization / LR Scheduling과 연결<br>**비교 범위:** Mixup·CutMix는 입력·label 변화 예제로 비교. 각 증강의 구현·하이퍼파라미터 탐색은 제외 |
| Training Techniques | 학습 방법 · 구현 기법 | 중요 | **포함 개념:** EMA · Gradient norm clipping · Gradient accumulation / Effective batch · AMP (FP16 / BF16 / Autocast / Gradient scaling)<br>**EMA·clipping:** EMA로 학습 중 가중치의 이동평균을 유지하는 목적과 갱신식, 큰 gradient norm을 제한하는 clipping의 원리를 작은 예제로 확인. EMA의 가중치 평균과 clipping의 gradient 조절을 구분하고 EMA teacher는 17회차에서 연결<br>**의도적 gradient 누적:** 2회차의 누적·초기화 원리를 짧게 복습하고, 이 회차 담당자가 준비한 예제로 작은 batch 여러 개의 gradient를 모아 한 번 갱신하는 흐름을 확인. Batch 크기 8로 4번 처리한 뒤 한 번 업데이트하는 effective batch 32 예제에서 loss의 평균 처리·zero_grad·optimizer.step 시점을 추적. BatchNorm 등으로 큰 batch와 항상 같은 결과가 되는 것은 아님을 구분<br>**AMP 묶음 소개:** 연산별로 정밀도를 섞어 속도·메모리 효율을 높이는 목적을 설명. FP16/BF16은 수치 형식, autocast는 연산별 자료형 선택, gradient scaling은 FP16에서 작은 gradient의 수치적 소실을 줄이는 방법이라는 관계까지만 정리<br>**학습 깊이:** EMA·clipping·gradient accumulation의 원리와 짧은 코드 흐름을 중심으로 다룸. AMP는 목적·용어 관계 위주로 소개하고, 비트 구조·GradScaler 사용 순서·AMP와 clipping/누적의 결합은 확장 학습으로 연결<br>**선택 심화:** Activation checkpointing은 중간 activation 일부의 저장을 생략하고 역전파 때 다시 계산해, 메모리 사용을 줄이는 대신 재계산 비용을 늘리는 기법으로 소개. 4회차의 학습 상태 파일 저장과 구분하며 상세 구현은 공통 학습 범위에 포함하지 않음 |

#### 0-B. Experiments & Analysis

##### 4회차 · 2026.11.26 (목) · 발표자: 김재순 · 실험 설계와 모델·feature 분석

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Experiments & Diagnostics | 분석 방법 | 필수 | **포함 개념:** Train / Validation / Test split · Data leakage · Random seed · Baseline / Ablation · Learning curves · Validation-based model selection · Best checkpoint / Early stopping · Model saving / Training resume · Small-subset overfit check · Failure cases<br>**실험 설계:** 데이터 분할·누수·seed 확인, baseline과 바꾼 요소·고정 조건 구분. seed·반복에 따른 결과 변동 확인<br>**결과 판단:** 준비된 학습·검증 곡선과 실패 사례에서 과적합·학습 불안정·잘못된 비교를 구분. 곡선의 기본 해석은 3회차 Regularization의 일반화 진단과 연결<br>**모델 선택과 중단:** 준비된 학습·검증 곡선에서 마지막 시점의 모델과 검증 지표가 가장 좋은 시점의 모델을 비교. Best checkpoint 선택과 early stopping의 학습 종료 결정을 구분하고, 지표의 개선 방향·확인 주기·patience를 짚음. Test set은 모델 선택·중단 판단에 사용하지 않고 최종 평가에 활용<br>**저장과 재개:** 추론용 model state 저장과 학습 재개를 구분. 재개에는 model·optimizer·진행 epoch/step과, 사용하는 경우 scheduler·AMP scaler·EMA 등의 상태도 복원해야 함을 저장 항목 표로 확인. 파일 저장·복원 전체 코드 구현과 동일 실행의 완전한 재현은 확장 학습으로 연결<br>**직접 판단:** 담당자가 준비한 ‘소수의 고정된 학습 샘플에서도 loss가 내려가지 않는 상황’의 코드·곡선을 보고 입력·target·gradient·파라미터 업데이트를 점검. 모델 용량·학습률도 함께 고려하며 원인 후보 하나와 이를 확인할 후속 실험 하나를 제안. 기존 진단 과제의 사례로 다루고, feature 시각화의 직접 실행·해석은 같은 회차의 Model & Embedding Analysis에서 연결 |
| Model & Embedding Analysis / Visualization | 분석 방법 | 필수 | **포함 개념:** Activation / Weight histograms · Mean / Standard deviation · Gradient norm · Feature extraction · L2 normalization · Cosine similarity / Top-k neighbors · PCA / Explained variance · t-SNE / Perplexity · UMAP / n_neighbors / min_dist · Random seed · Visualization pitfalls<br>**층별 통계:** 각 층의 activation·weight 히스토그램과 평균·표준편차, gradient norm을 코드로 수집·표시. 초기화 크기를 바꿔 출력 분포·ReLU 출력의 0 비율·gradient 크기 변화 비교. 동일 모델·batch·loss 조건에서 관찰하며, 작은 gradient나 높은 0 비율만으로 고장 원인을 확정하지 않음<br>**유사도 검색:** 분석할 layer의 feature를 추출·L2 정규화하고, query의 cosine similarity 상위 k개 원본 이미지를 표시. 자기 자신을 제외하고 query·layer를 바꿔 가까운 샘플이 공유하는 속성 확인<br>**PCA:** 준비된 동일 feature 집합을 2차원으로 투영하고 class별 산점도·설명 분산 확인. 분산이 큰 방향을 찾는 PCA를 비선형 시각화와 비교할 기준으로 사용<br>**t-SNE:** 고차원에서 가까운 샘플의 관계를 저차원 배치에 반영하는 직관 확인. 같은 표본·전처리에서 perplexity를 바꿔 이웃과 군집 모양의 변화 비교, seed를 바꾼 결과와 함께 확인<br>**UMAP:** 이웃 그래프를 바탕으로 저차원 배치를 만드는 직관 확인. n_neighbors·min_dist를 한 번에 하나씩 바꿔 이웃 범위·점들의 밀집도 변화 관찰, 같은 feature의 PCA·t-SNE 결과와 비교<br>**해석과 검증:** class 색을 보기 전후 해석을 비교하고, 군집 간 거리·군집 크기·분리만으로 의미 관계나 표현 품질을 단정할 수 없는 이유 설명. 의심되는 샘플은 원래 feature 공간의 이웃과 원본 이미지로 확인하며, UMAP의 군집 간 거리도 그대로 해석하지 않음<br>**실습 방식과 범위:** 담당자가 학습된 작은 모델·고정 입력·소규모 feature·이미지·label과 실행을 확인한 노트북을 미리 제공. 참여자는 통계 수집·검색·각 시각화의 짧은 셀 실행, 설정 한 가지 변경, 결과 비교에 집중. 새 모델 훈련·환경 설정·수집 코드 전체 구현·알고리즘 전체 유도는 포함하지 않음 |

### 1. Transformer와 비전·멀티모달 모델

#### 학습 목표

Attention의 계산에서 Transformer 블록·학습·생성으로 연결하고, 이미지의 토큰화·위치 표현과 연산·메모리 효율화를 설명한다. 공통 구조를 익힌 뒤 객체 검출·밀집 예측·프롬프트 분할·멀티모달 응답 생성에 적용하며, 과제별 입력·출력·학습 신호·정보 결합 방식을 비교한다.

#### 학습 내용

#### 1-A. Transformer Foundations

##### 5회차 · 2026.12.03 (목) · 발표자: 곽명조 · Attention: 토큰 사이의 정보 결합

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Attention | 기초 연산 | 필수 | **포함 개념:** Query / Key / Value · Scaled dot-product attention · Softmax axis · Self-attention / Cross-attention · Multi-head attention · Causal / Padding mask · Tensor shape / Computation cost · Permutation equivariance / Position information<br>**필요성:** 토큰마다 필요한 문맥을 다른 토큰에서 가져오는 방식, 입력에 따라 달라지는 정보 결합<br>**계산 흐름:** Q·K·V의 projection과 shape → QKᵀ·√d_k 스케일링 → mask·softmax → V의 가중합 → head 결합·출력 projection. 작은 입력에서 값·차원·softmax 축을 추적<br>**정보의 출처와 범위:** self-attention과 cross-attention에서 Q·K·V를 가져오는 입력, query·key 길이가 다를 때의 출력 shape, causal·padding mask가 허용하는 정보 범위를 비교<br>**계산 비용과 위치:** 토큰 수에 따른 attention 행렬·연산·메모리 증가. 위치 정보와 순서 의존 mask가 없을 때의 permutation equivariance를 확인하고, 순서·공간 배치를 별도로 전달해야 하는 이유를 설명<br>**Query 용어:** attention의 Q는 입력 표현을 projection해 만드는 조회 벡터의 계산 역할. learned query token은 모델이 학습하는 표현이며, attention에서 Q·K·V를 만드는 입력이 될 수 있다는 점을 구분<br>**학습 범위:** 작은 self/cross-attention·mask 예제로 계산을 완성. FlashAttention·cache는 8회차에서 연결 |

<!-- study-references:5 -->

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)

<!-- /study-references -->

##### 6회차 · 2026.12.10 (목) · 발표자: 박준규 · Transformer: 블록 구조와 학습·생성

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Transformer Architecture | 모델 구조 | 필수 | **포함 개념:** Token embedding · Sinusoidal positional encoding · Encoder / Decoder · FFN · Residual connection · LayerNorm / RMSNorm · Pre-Norm / Post-Norm · GPT / BERT · Next-token prediction · Masked language modeling · Training / Generation<br>**입력과 위치:** token embedding과 sinusoidal positional encoding의 역할·차원, 고정된 위치 표현과 학습하는 위치 embedding의 차이를 확인<br>**전체 구조:** encoder의 self-attention·FFN과 decoder의 causal self-attention·cross-attention·FFN을 연결. 한 블록과 전체 encoder–decoder의 입력·출력·residual·normalization 위치를 추적<br>**블록의 역할:** attention은 token 사이의 정보를 결합하고, 기본 position-wise FFN은 각 token의 채널 표현을 같은 가중치로 독립 변환. Pre-Norm·Post-Norm의 순서·gradient 경로와 LayerNorm·RMSNorm의 차이를 0장에 연결<br>**GPT·BERT 비교:** GPT의 decoder-only·causal attention·한 칸 이동한 next-token target과 BERT의 encoder-only·양방향 attention·MLM target을 비교. 접근 가능한 정보·loss 위치·출력 head를 작은 예제로 확인<br>**학습과 생성:** 정답 문맥으로 여러 위치의 loss를 병렬 계산하는 GPT 학습과, 이전 출력 token에 의존하는 자기회귀 생성을 구분. 한 번의 학습 forward와 두 번의 생성 step을 추적<br>**학습 범위:** 공통 블록·전체 정보 흐름을 중심으로 다루고 GPT·BERT는 구조·정보 범위·목표의 비교 사례로 사용. 모델별 전체 재현·세대별 발전사는 확장 학습으로 연결 |

<!-- study-references:6 -->

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- [Language Models are Unsupervised Multitask Learners](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
- [On Layer Normalization in the Transformer Architecture](https://arxiv.org/abs/2002.04745)

<!-- /study-references -->

##### 7회차 · 날짜 미정 · 발표자: 미정 · Vision Transformer: ViT·Swin과 공간 표현

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| ViT / Swin Transformer | 모델 · Backbone | 필수 | **포함 개념:** ViT · Patch embedding · CLS token / Readout · Learned positional embedding · Global attention · Swin Transformer · Window / Shifted-window attention · Patch merging · Relative position bias · Multi-scale features<br>**ViT 전체 흐름:** 이미지 → patch·Linear projection → CLS·위치 embedding → encoder → 분류 출력을 먼저 완성. 이미지 크기·patch 크기에 따른 token 수와 각 단계의 shape를 추적<br>**공간 정보와 출력:** ViT의 learned absolute position과 해상도 변경 시 위치 embedding 보간, 원 모델의 CLS readout과 pooling 변형을 비교. patch 위치와 token 순서의 대응을 확인<br>**Swin의 핵심 변화:** window 내부 attention → shifted window의 정보 교환 → patch merging을 따라 해상도·채널 변화를 확인. 상대 위치 bias의 적용 위치를 연결<br>**Backbone 비교:** ViT의 전역 attention·일정한 token 해상도와 Swin의 국소 attention·계층적 feature를 비교. dense prediction에 전달하는 출력과 데이터 규모·입력 해상도·계산 비용의 관계를 해석<br>**학습 범위:** ViT의 입력부터 출력까지를 중심으로 Swin의 window·shift·계층 구조를 비교. 세부 구현 최적화와 모든 변형의 상세 유도는 확장 학습으로 연결 |
| Positional Encoding Variants | 구성 요소 | 중요 | **포함 개념:** Sinusoidal / Learned absolute position · Relative position bias · RoPE · Embedding / Attention score / Q–K injection · 1D / 2D position · Sequence length / Resolution change<br>**모델에서 비교:** 6회차의 sinusoidal encoding과 앞서 본 ViT의 absolute position·Swin의 relative position bias를 기준으로, 위치 정보를 embedding·attention score 중 어디에 넣는지 정리<br>**RoPE:** Q·K에 위치별 회전을 적용하고 두 token의 상대 위치가 내적에 반영되는 핵심 원리·적용 지점을 작은 예제로 확인<br>**학습 범위:** 1D·2D 위치, 길이·해상도 변경의 차이와 세 방식의 적용 위치를 비교. 위치 표현의 전체 분류·긴 문맥 확장 기법·RoPE 전체 수식 증명은 확장 학습으로 연결 |

<!-- study-references:7 -->

- [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929)
- [Swin Transformer: Hierarchical Vision Transformer using Shifted Windows](https://arxiv.org/abs/2103.14030)
- [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)

<!-- /study-references -->

##### 8회차 · 날짜 미정 · 발표자: 미정 · Transformer 효율화: FlashAttention·KV cache

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Efficient Attention / KV Cache | 모델 구조 · 구현 기법 | 중요 | **포함 개념:** Attention computation / Memory cost · FlashAttention · Tiling / Online softmax · GPU memory IO · KV cache · Autoregressive generation · Prefill / Decode · MHA / MQA / GQA · Query heads / Key–Value heads · KV sharing / Cache shape · Memory–Computation trade-off<br>**비용의 출처:** 7회차의 patch token 수와 6회차의 자기회귀 생성을 출발점으로, projection·attention 행렬·중간 결과 저장·반복 계산의 비용을 구분<br>**FlashAttention:** tiling·online softmax로 수학적으로 같은 dense attention을 계산하며 GPU 메모리 이동·중간 행렬 저장을 줄이는 원리. Dense attention의 연산량은 token 수에 대해 여전히 이차적으로 증가<br>**KV cache:** 자기회귀 생성에서 이전 token의 K·V를 저장·재사용하는 조건, prefill과 token별 decode, 층별 cache shape·메모리 증가를 작은 예제로 추적<br>**MHA·MQA·GQA:** query head별 K·V를 유지하는 MHA, 하나를 공유하는 MQA, 그룹별로 공유하는 GQA의 projection·head 대응·cache 저장량을 비교<br>**효율화의 구분:** FlashAttention의 계산 순서·IO, cache의 계산 재사용, MQA/GQA의 KV head 공유를 구분. 품질·메모리·추론 비용은 같은 모델·길이·장비 등 비교 조건을 확인<br>**학습 범위:** shape·저장량·한 번의 decode 흐름을 중심으로 다룸. GPU kernel 구현·세부 성능 튜닝·checkpoint 변환 학습은 확장 학습으로 연결 |

<!-- study-references:8 -->

- [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://arxiv.org/abs/2205.14135)
- [Efficiently Scaling Transformer Inference](https://arxiv.org/abs/2211.05102)
- [FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning](https://arxiv.org/abs/2307.08691)
- [Fast Transformer Decoding: One Write-Head is All You Need](https://arxiv.org/abs/1911.02150)
- [GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](https://arxiv.org/abs/2305.13245)

<!-- /study-references -->

#### 1-B. Vision & Multimodal Models

##### 9회차 · 날짜 미정 · 발표자: 미정 · 객체 검출: DETR·Deformable DETR

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DETR / Deformable DETR | 모델 | 필수 | **포함 개념:** DETR · Set prediction · Learned object query / Output slots · CNN backbone / Transformer encoder–decoder · Bipartite / Hungarian matching · Matching cost / Training loss · No-object class · Bounding box prediction · NMS-free inference · Deformable DETR · Reference points / Sampling offsets / Attention weights · Bilinear sampling / Multi-scale deformable attention<br>**필요성과 입력:** 순서가 없는 객체 정답 집합을 고정 개수의 class·box 예측에 대응시키는 문제. Backbone을 feature map·stride·채널을 반환하는 모듈로 읽고, 1×1 projection과 위치 정보가 encoder 입력으로 연결되는 shape를 확인<br>**DETR 구조와 query:** feature → encoder → learned object query를 사용하는 decoder → class·box 출력. Object query는 출력 slot을 구분하는 학습 표현이며 attention에서 계산하는 Q와 역할·출처를 구분<br>**DETR 학습·추론:** 작은 객체 집합으로 Hungarian matching 비용과 matching 후의 class·box loss를 구분. Unmatched query의 no-object 처리, 고정 출력 slot과 NMS 없는 추론의 관계를 확인<br>**Deformable DETR:** 원 DETR의 수렴·고해상도 feature 처리 문제에서 출발. Query가 reference point 주변 offset·weight를 예측하고 소수 위치의 feature를 bilinear sampling·가중합하는 흐름과 multi-scale 참조를 비교<br>**근거와 비교 범위:** DETR의 전체 학습·추론을 중심으로 Deformable DETR의 참조 위치·가중치 생성·수렴·작은 객체 성능 변화를 확인. YOLOv10은 one-to-many/one-to-one head·NMS-free 추론의 짧은 비교와 Related Work로 연결 |

<!-- study-references:9 -->

- [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872)
- [YOLOv10: Real-Time End-to-End Object Detection](https://arxiv.org/abs/2405.14458)
- [Deformable DETR: Deformable Transformers for End-to-End Object Detection](https://arxiv.org/abs/2010.04159)

<!-- /study-references -->

##### 10회차 · 날짜 미정 · 발표자: 미정 · 밀집 예측: DPT와 공간 해상도 복원

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Dense Prediction / DPT | 모델 | 필수 | **포함 개념:** Dense prediction · Depth / Semantic segmentation · ViT / Hybrid backbone · Intermediate tokens · Reassemble · Spatial feature map · Multi-resolution fusion · Convolution / Upsampling · Convolutional decoder<br>**필요성과 출력:** 이미지 단위 표현을 픽셀별 깊이·범주 출력으로 바꾸는 문제. Token의 공간 대응과 전역 문맥을 유지하며 출력 해상도를 복원하는 decoder의 역할을 설명<br>**필요한 공간 연산:** Feature map의 채널·공간 축, 1×1/3×3 convolution·보간/upsampling·feature fusion을 DPT의 shape를 읽을 정도로 보충하고 각각 입력·출력 해상도와 정보 결합 역할을 확인<br>**DPT 전체 흐름:** Backbone 여러 층의 token → reassemble·해상도 변환 → 여러 해상도의 spatial feature → convolutional decoder의 점진적 fusion → 픽셀별 출력을 추적<br>**학습과 구조 비교:** 깊이·semantic segmentation의 target·출력 채널·loss를 비교. Vanilla ViT의 중간 층이 처음부터 해상도 pyramid인 것은 아니라는 점과 Swin의 계층적 feature·DPT의 해상도 재구성 차이를 구분<br>**학습 범위:** Token에서 공간 출력으로 이어지는 공통 head 구조를 중심으로 다룸. Depth Anything·DUSt3R·VGGT 등은 DPT 계열 head의 활용 사례로 연결하고 각 전체 모델은 Related Work로 확장 |

<!-- study-references:10 -->

- [Vision Transformers for Dense Prediction](https://arxiv.org/abs/2103.13413)
- [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193)
- [Depth Anything: Unleashing the Power of Large-Scale Unlabeled Data](https://arxiv.org/abs/2401.10891)
- [Depth Anything V2](https://arxiv.org/abs/2406.09414)
- [DUSt3R: Geometric 3D Vision Made Easy](https://arxiv.org/abs/2312.14132)
- [VGGT: Visual Geometry Grounded Transformer](https://arxiv.org/abs/2503.11651)

<!-- /study-references -->

##### 11회차 · 날짜 미정 · 발표자: 미정 · SAM 계열: 프롬프트 분할·추적과 3D 확장

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| SAM Family | 모델 · 생성 모델 | 중요 | **포함 개념:** SAM · Image / Prompt encoder · Point / Box / Mask prompt · Learned mask / Output tokens · Two-way mask decoder / Cross-attention · Multiple masks / Quality prediction · Image embedding reuse · Prompt sampling / Mask loss · Data engine · SAM 2 / Memory encoder / Memory bank / Memory attention · SAM 3 / Concept prompts / Detector–Tracker / Presence head · SAM 3.1 / Object Multiplex · SAM 3D Objects / Generative prior · SAM 3D Body / MHR / Human mesh recovery<br>**문제와 출력:** 점·박스가 지정한 대상 mask, 비디오에서 유지할 mask·ID, 개념에 해당하는 모든 instance, 단일 이미지의 3D 객체·인체를 구분. 계열별 입력·조건·출력을 한 표로 비교<br>**원 SAM 중심 학습:** Image encoder·prompt encoder·two-way mask decoder → 여러 mask·품질 예측의 정보 흐름·shape를 추적. Prompt sampling·mask loss·image embedding 재사용과 data engine의 역할을 확인<br>**Token과 query:** 입력 prompt token·learned mask/output token·attention의 Q를 구분. DETR의 출력 slot, DPT의 픽셀별 출력과 연결해 prompt가 가리키는 대상의 mask를 만드는 과정을 설명<br>**SAM 2의 시간 확장:** 현재 frame feature → memory attention → mask → memory encoder·bank 갱신의 핵심 흐름. 과거 대상 정보·현재 prompt와 가림·재등장의 관계를 원 SAM과 비교<br>**SAM 3·3.1 비교:** SAM 3의 text/image exemplar 기반 concept prompt·detector–tracker·presence 판단, SAM 3.1의 Object Multiplex 공유 memory·여러 객체 공동 처리를 새 입력·출력·정보 흐름 중심으로 비교<br>**SAM 3D 비교:** Objects의 이미지·대상 mask → geometry/layout → texture/detail과 mesh/Gaussian splat 출력, Body의 이미지·선택적 keypoint/mask → MHR 기반 pose·human mesh를 비교. 관측과 generative prior로 채우는 영역을 구분<br>**학습 깊이:** 원 SAM을 자세히 다루고 SAM 2의 memory를 주요 확장으로 설명. 나머지 계열은 문제·구조 변화 비교로 모두 다루며, 3D의 생성 loss·flow·latent 세부 원리는 3장 학습 후 다시 연결 |

<!-- study-references:11 -->

- [Segment Anything](https://arxiv.org/abs/2304.02643)
- [SAM 2: Segment Anything in Images and Videos](https://arxiv.org/abs/2408.00714)
- [SAM 3: Segment Anything with Concepts](https://arxiv.org/abs/2511.16719)
- [SAM 3.1](https://huggingface.co/facebook/sam3.1/blob/main/README.md)
- [SAM 3D: 3Dfy Anything in Images](https://arxiv.org/abs/2511.16624)
- [SAM 3D Body: Robust Full-Body Human Mesh Recovery](https://arxiv.org/abs/2602.15989)

<!-- /study-references -->

##### 12회차 · 날짜 미정 · 발표자: 미정 · Multimodal LLMs: 이미지 표현과 언어 모델 연결

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Multimodal LLMs / Visual Tokens | 모델 | 중요 | **포함 개념:** LLaVA / LLaVA-1.5 · Pretrained vision encoder / Projector / LLM · Continuous visual tokens / Image–Text sequence · Feature alignment / Instruction tuning · Frozen / Trainable parameters · Next-token loss / Response generation · BLIP-2 / Q-Former · Learned query tokens / Cross-attention · Flamingo / Gated cross-attention · Qwen2-VL / Dynamic resolution / M-RoPE<br>**선수 개념과 문제:** 사전학습 encoder·LLM을 재사용하고, frozen/fine-tuning의 고정·갱신 파라미터를 먼저 설명. CLIP은 이미지·텍스트 표현을 정렬한 encoder의 예로 소개하고 대조 학습 loss는 14회차에서 다룸. 여기서는 이미지를 근거로 언어 응답을 생성하는 연결 구조에 집중<br>**LLaVA 전체 흐름:** Vision encoder → projector → visual token을 text token과 함께 decoder-only LLM에 입력 → 응답 생성. 원 LLaVA의 linear projector와 LLaVA-1.5의 MLP projector를 구분하고 token 수·차원·입력 위치를 추적<br>**LLaVA 학습·생성:** 원 LLaVA의 feature alignment는 projector, instruction tuning은 projector·LLM을 학습하며 vision encoder는 고정. 단계별 데이터·응답 target·loss mask·gradient 경로와 생성 시 이전 token을 사용하는 흐름을 확인<br>**BLIP-2 주요 비교:** 고정 vision encoder → learned query가 image feature를 cross-attention으로 읽는 Q-Former → projection → 고정 LLM. 고정 개수 visual token·정보 추출 방식과 두 단계 학습의 목적·고정 범위를 LLaVA와 비교<br>**대표 확장 비교:** Flamingo는 resampler·LM 내부 gated cross-attention의 결합 위치, Qwen2-VL은 해상도에 따른 visual token 수와 M-RoPE의 공간·시간 위치 표현까지만 비교. 모델별 전체 학습 과정은 Related Work로 확장<br>**Token의 뜻과 학습 범위:** Visual token은 이 모델들에서 연속 feature 벡터이며 21회차 VQ code index와 구분. LLaVA를 중심으로 BLIP-2를 주요 비교 대상으로 삼고, learned query와 계산된 Q·token 수·결합 위치·학습 목표·고정 범위를 같은 기준으로 정리 |

<!-- study-references:12 -->

- [Visual Instruction Tuning](https://arxiv.org/abs/2304.08485)
- [Improved Baselines with Visual Instruction Tuning](https://arxiv.org/abs/2310.03744)
- [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://arxiv.org/abs/2301.12597)
- [Flamingo: a Visual Language Model for Few-Shot Learning](https://arxiv.org/abs/2204.14198)
- [Qwen2-VL: Enhancing Vision-Language Model's Perception of the World at Any Resolution](https://arxiv.org/abs/2409.12191)
- [Qwen3-VL Technical Report](https://arxiv.org/abs/2511.21631)
- [InternVL3.5: Advancing Open-Source Multimodal Models in Versatility, Reasoning, and Efficiency](https://arxiv.org/abs/2508.18265)
- [PaliGemma: A versatile 3B VLM for transfer](https://arxiv.org/abs/2407.07726)
- [DeepSeek-VL2: Mixture-of-Experts Vision-Language Models for Advanced Multimodal Understanding](https://arxiv.org/abs/2412.10302)
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)

<!-- /study-references -->

### 2. 표현 학습과 모델 적응

#### 학습 목표

표현의 평가·전이 기준을 먼저 익힌 뒤, 대조 학습·가린 영역 예측·teacher–student 학습·반지도 학습의 target과 gradient 경로를 비교한다. Class label·이미지–텍스트 쌍·pixel·teacher의 분포/feature가 각각 어떤 학습 신호를 주는지 구분한다. 전역 표현·밀집 특징·추가 조정 후 성능을 나누어 평가하고, 데이터·label 가용성·분포 변화·모델 적응 범위에 맞춰 결과를 해석한다.

#### 학습 내용

##### 13회차 · 날짜 미정 · 발표자: 미정 · 사전학습과 전이: 표현 평가·모델 적응

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Pretraining & Transfer | 학습 방법 · 적응 방법 | 필수 | **포함 개념:** Pretraining / Downstream task · Supervised / Self-supervised / Image–text supervision · Backbone / Head · Frozen features · Linear probing / k-NN · Partial / Full fine-tuning · LoRA / Low-rank update · Parameter freezing / Gradient flow · Trainable parameters / Memory · Evaluation protocol<br>**평가 기준부터:** 사전학습 → encoder feature 추출 → frozen feature 평가 또는 새 작업에 맞춘 조정의 흐름. 12회차에서 사용한 사전학습 모델의 학습 신호·데이터·head를 구분하고 이후 표현 학습을 평가할 공통 기준을 마련<br>**표현 평가와 조정:** k-NN은 저장한 feature와 label로 이웃을 비교하고, linear probing은 encoder를 고정한 채 선형 head를 학습. 부분/전체 fine-tuning의 고정·갱신 파라미터와 gradient 경로를 비교하고 조정 후 성능을 frozen feature 품질과 구분<br>**LoRA:** 고정 가중치에 ΔW = BA를 더하는 저랭크 변화량 학습. 작은 Linear 예제로 A/B의 shape·rank·scale·초기화와 gradient 경로·학습 파라미터 수를 확인<br>**비용과 근거:** 학습 파라미터·optimizer state·activation·전체 모델 저장 비용을 나누고 LoRA가 모든 학습 메모리를 같은 비율로 줄이는 것은 아님을 확인. 사전학습 데이터·backbone·head·조정 예산·평가 데이터 중복을 맞춰 비교<br>**학습 범위:** 표현 평가와 고정/갱신 범위를 중심으로 LoRA의 한 번 forward·gradient 경로를 추적. 대규모 fine-tuning recipe·양자화·모든 적응 기법은 확장 학습으로 연결 |
| Domain Shift & Generalization | 기초 개념 | 중요 | **포함 개념:** Source / Target domains · Distribution shift / Dataset bias · Synthetic-to-real · Domain adaptation / Generalization · Target data / Labels · Model selection / Evaluation protocol<br>**문제 상황:** 같은 작업에서 카메라·조명·데이터 출처가 바뀔 때의 성능 변화. Source·target의 입력 분포와 label 가용성을 작은 사례로 명시<br>**설정 구분:** Target 데이터를 조정에 사용하는 domain adaptation과, 학습 중 보지 않은 target domain으로의 일반화를 평가하는 domain generalization을 구분. Target의 비라벨 데이터·label·test-time 갱신 허용 여부를 함께 기록<br>**평가 조건과 범위:** 학습·모델 선택·조정·최종 평가에서 접근한 데이터와 label을 구분. 분포 변화 자체에 대한 일반화와 target 사용 효과를 나누어 해석하고, DANN 등 개별 adaptation 알고리즘은 Related Work로 확장 |

<!-- study-references:13 -->

- [How transferable are features in deep neural networks?](https://arxiv.org/abs/1411.1792)
- [Do Better ImageNet Models Transfer Better?](https://arxiv.org/abs/1805.08974)
- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- [In Search of Lost Domain Generalization](https://arxiv.org/abs/2007.01434)
- [WILDS: A Benchmark of in-the-Wild Distribution Shifts](https://arxiv.org/abs/2012.07421)
- [Domain-Adversarial Training of Neural Networks](https://arxiv.org/abs/1505.07818)

<!-- /study-references -->

##### 14회차 · 날짜 미정 · 발표자: 미정 · 대조 학습: SimCLR과 이미지–텍스트 정렬

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Contrastive Learning | 학습 방법 | 필수 | **포함 개념:** SimCLR · Positive / Negative pairs · Data augmentation · Encoder / Projection head · Normalized embeddings · NT-Xent loss / Temperature · Batch negatives · Representation / Projection · Linear evaluation · MoCo<br>**학습 신호:** 같은 이미지의 두 증강을 positive로, batch의 다른 이미지를 negative로 사용하는 목표. 증강이 보존해야 할 정보와 같은 의미의 다른 이미지가 negative가 될 수 있는 한계를 확인<br>**계산과 loss:** 두 view → encoder → projection → 정규화·유사도 행렬 → NT-Xent. 작은 batch에서 자기 자신 제외·positive 위치·negative·temperature와 loss를 추적<br>**활용과 설계 근거:** loss에 사용하는 projection과 downstream representation을 구분하고 13회차의 frozen encoder 평가에 연결. 증강·batch 크기·projection head의 영향을 같은 조건의 ablation으로 확인<br>**학습 범위:** SimCLR의 target·유사도·loss·평가 흐름을 중심으로 다룸. MoCo는 queue·momentum encoder로 negative를 구성하는 대표 비교로 연결하고 전체 구현은 Related Work로 확장 |
| Image–Text Alignment | 모델 · 학습 방법 | 필수 | **포함 개념:** CLIP · SigLIP / SigLIP 2 · Image / Text encoders · Paired image–text data · Normalized embeddings · Similarity matrix · Bidirectional softmax / Pairwise sigmoid loss · Temperature / Scale / Bias · Zero-shot classification / Retrieval<br>**CLIP 전체 흐름:** 이미지–텍스트 쌍 → 두 encoder → 정규화된 embedding → batch 유사도 행렬. SimCLR의 두 이미지 view와 다른 positive의 출처, 이미지→텍스트·텍스트→이미지 양방향 softmax loss를 비교<br>**SigLIP 주요 비교:** pair별 일치/불일치를 학습하는 sigmoid loss의 target·scale·bias와 CLIP의 batch softmax 정규화를 작은 행렬로 비교. Batch 의존성이 줄어드는 지점과 negative 구성의 영향을 구분<br>**Zero-shot과 활용:** class prompt → text embedding → 이미지와의 유사도로 분류하고, 검색·12회차 MLLM의 vision encoder 재사용에 연결. Zero-shot은 해당 분류 head의 추가 학습이 없다는 뜻이며 학습 데이터 중복 여부는 별도로 확인<br>**후속 연구와 범위:** CLIP의 학습·추론을 중심으로 SigLIP의 loss를 비교. SigLIP 2는 이미지–텍스트 정렬에 captioning·self-distillation·masked prediction 등을 결합한 확장으로 소개하고, 세부 학습 recipe는 15·17회차 및 Related Work에 연결 |

<!-- study-references:14 -->

- [A Simple Framework for Contrastive Learning of Visual Representations](https://arxiv.org/abs/2002.05709)
- [Learning Transferable Visual Models From Natural Language Supervision](https://arxiv.org/abs/2103.00020)
- [Sigmoid Loss for Language Image Pre-Training](https://arxiv.org/abs/2303.15343)
- [Momentum Contrast for Unsupervised Visual Representation Learning](https://arxiv.org/abs/1911.05722)
- [SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://arxiv.org/abs/2502.14786)

<!-- /study-references -->

##### 15회차 · 날짜 미정 · 발표자: 미정 · Masked Image Modeling: MAE의 표현 학습

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Masked Image Modeling | 학습 방법 | 필수 | **포함 개념:** MAE · Patch masking · Visible-token encoder · Mask token / Position · Asymmetric encoder–decoder · Pixel reconstruction / Masked-region loss · Downstream transfer · Pixel / Token / Feature targets<br>**학습 목표:** 가린 영역을 문맥으로 예측하며 encoder 표현을 학습. Pixel 복원 오차와 downstream 표현 품질을 서로 다른 평가로 구분<br>**MAE 전체 흐름:** Patch masking → 보이는 patch만 encoder에 입력 → 원래 공간 순서로 배치·mask token 추가 → 가벼운 decoder → pixel 복원. Encoder와 decoder의 token 수·위치 정보·shape를 추적<br>**Target과 loss:** 원 이미지의 가린 patch pixel을 target으로 사용하는 loss 위치, pixel normalization의 선택을 확인. Mask 비율·encoder의 sparse 입력·decoder 크기와 계산량을 비교<br>**학습 후 활용:** 복원용 decoder를 제거하고 encoder를 전이하는 과정과 linear probing/fine-tuning 평가를 13회차에 연결. 좋은 복원이 곧 좋은 semantic feature를 뜻하지는 않음을 실험 조건과 함께 해석<br>**다른 target과 범위:** MAE를 중심으로 BEiT의 discrete token target·I-JEPA의 feature target을 출력의 종류만 비교. 모든 masked prediction을 pixel 복원으로 묶지 않고, tokenizer·EMA target network의 상세 학습은 17·21회차 및 Related Work로 연결 |

<!-- study-references:15 -->

- [Masked Autoencoders Are Scalable Vision Learners](https://arxiv.org/abs/2111.06377)
- [BEiT: BERT Pre-Training of Image Transformers](https://arxiv.org/abs/2106.08254)
- [Self-Supervised Learning from Images with a Joint-Embedding Predictive Architecture](https://arxiv.org/abs/2301.08243)

<!-- /study-references -->

##### 16회차 · 날짜 미정 · 발표자: 미정 · Knowledge Distillation: teacher의 예측을 학습 신호로

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Knowledge Distillation | 학습 방법 | 필수 | **포함 개념:** Teacher / Student · Logits / Soft targets · Temperature / T-squared scaling · Cross-entropy / KL divergence · Soft-target / Hard-label losses · Frozen teacher / Stop-gradient · Feature distillation<br>**전달할 정보:** 정답 class 외에 teacher의 class 간 출력 분포가 주는 정보를 student에 전달. 모델 압축·지식 전이의 목적과 teacher 예측이 실제 정답과 다를 수 있음을 설명<br>**기본 학습 흐름:** 학습된 고정 teacher → temperature로 만든 soft target, student → soft-target loss와 실제 label loss → student만 갱신. 작은 class 예제로 target·loss 위치·gradient를 추적<br>**Temperature와 loss:** Temperature에 따른 분포 변화, hard-label/soft-target loss의 결합·가중치와 T² 스케일 보정의 목적을 확인. 고정 teacher target에서 cross-entropy와 KL의 student gradient 관계를 비교<br>**확장과 범위:** 출력 분포 distillation을 중심으로 FitNets의 중간 feature 전달을 비교 사례로 연결. Teacher가 고정된 기본 KD와 다음 회차의 EMA teacher를 구분하고, 더 큰 teacher가 항상 더 좋은 student를 보장하지 않는 조건을 확인 |

<!-- study-references:16 -->

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531)
- [FitNets: Hints for Thin Deep Nets](https://arxiv.org/abs/1412.6550)

<!-- /study-references -->

##### 17회차 · 날짜 미정 · 발표자: 미정 · Self-Distillation: DINO 계열의 표현 학습

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Self-Distillation | 학습 방법 | 필수 | **포함 개념:** DINO / DINOv2 / DINOv3 · Teacher / Student · Multi-crop · EMA / Stop-gradient · Output distributions / Prototypes · Centering / Sharpening / Collapse · iBOT / Masked-patch targets · Gram teacher / Gram anchoring · Global / Dense feature evaluation · BYOL / Registers<br>**원 DINO 중심 학습:** 같은 이미지의 서로 다른 crop → teacher의 출력 분포 → student의 cross-entropy 학습. Global teacher view·global/local student view·동일 view 쌍 제외·target 위치를 추적하며 출력 차원이 사람의 class label을 뜻하지 않음을 구분<br>**Teacher와 collapse:** Student의 gradient 갱신과 teacher의 EMA 갱신·stop-gradient를 분리. 원 DINO의 centering·temperature sharpening이 균일/상수 출력 같은 collapse와 어떤 관계가 있는지 확인하고 EMA만으로 모든 안정화가 설명되는 것은 아님을 구분<br>**DINOv2와 iBOT:** 이미지 수준 DINO objective와 가린 patch의 teacher 분포를 예측하는 iBOT objective의 입력·target·loss 위치를 비교. MAE의 pixel target과 차이, curated data·규모·안정화 기법의 기여를 함께 확인<br>**DINOv3와 Gram anchoring:** 장시간 학습에서 전역 성능과 밀집 특징 품질이 다르게 변할 수 있다는 문제에서 출발. 정규화한 patch feature의 Gram matrix를 Gram teacher의 관계에 맞추는 목표를 읽고, 기본 EMA teacher와 별도 기준 역할·초기 checkpoint·주기적 갱신을 구분<br>**대표 변화와 평가:** DINOv3의 target balancing 변경·Gram anchoring을 원 DINO의 centering과 구분하고, CLS/global feature·patch/dense feature를 각각 평가. BYOL·register token은 target 형식·feature artifact를 보는 관련 비교로 연결<br>**학습 깊이:** 원 DINO의 학습 step을 완성하고 v2는 image/patch target, v3는 Gram 관계의 추가 목표를 중심으로 비교. 모든 버전의 전체 loss·최적화 recipe와 BYOL·register의 상세 구현은 Related Work로 확장 |

<!-- study-references:17 -->

- [Emerging Properties in Self-Supervised Vision Transformers](https://arxiv.org/abs/2104.14294)
- [DINOv2: Learning Robust Visual Features without Supervision](https://arxiv.org/abs/2304.07193)
- [DINOv3](https://arxiv.org/abs/2508.10104)
- [Bootstrap your own latent: A new approach to self-supervised Learning](https://arxiv.org/abs/2006.07733)
- [iBOT: Image BERT Pre-Training with Online Tokenizer](https://arxiv.org/abs/2111.07832)
- [Vision Transformers Need Registers](https://arxiv.org/abs/2309.16588)

<!-- /study-references -->

##### 18회차 · 날짜 미정 · 발표자: 미정 · 반지도 학습: FixMatch와 pseudo-label

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Semi-Supervised Learning | 학습 방법 | 중요 | **포함 개념:** Labeled / Unlabeled data · FixMatch · Pseudo-labels / Confidence threshold · Weak / Strong augmentation · Consistency regularization · Supervised / Unsupervised losses · Stop-gradient · Confirmation bias · Mean Teacher / Adaptive thresholds<br>**문제와 target:** 일부 이미지에만 class label이 있을 때 unlabeled 이미지를 함께 활용하는 문제. DINO의 표현 학습 target과 알려진 class에 대한 pseudo-label을 구분<br>**FixMatch 전체 흐름:** 동일 network의 weak augmentation 예측 → confidence threshold → argmax pseudo-label → strong augmentation의 target. 독립된 EMA teacher가 필수인 구조로 오해하지 않도록 두 branch와 target 분리를 명시<br>**Loss와 gradient:** Labeled supervised loss와 confidence mask를 적용한 unlabeled loss를 결합. 작은 class 예제로 통과/제외 샘플·target stop-gradient·strong branch의 gradient를 추적<br>**실패 조건과 평가:** 잘못된 pseudo-label의 반복 학습·class 불균형·확신도 오판·의미를 바꾸는 증강을 확인. 실제 label 수·사전학습·unlabeled 접근 조건·불균형 정도·평가 분할을 맞춰 비교<br>**후속 연구와 범위:** FixMatch를 중심으로 Mean Teacher의 weight-averaged target, FlexMatch·FreeMatch의 threshold 적응을 대표 변화로 비교. 반지도 분류·domain adaptation·class 밖의 unlabeled data는 가정이 다름을 구분하고 세부 알고리즘은 Related Work로 확장 |

<!-- study-references:18 -->

- [FixMatch: Simplifying Semi-Supervised Learning with Consistency and Confidence](https://arxiv.org/abs/2001.07685)
- [Mean teachers are better role models: Weight-averaged consistency targets improve semi-supervised deep learning results](https://arxiv.org/abs/1703.01780)
- [FlexMatch: Boosting Semi-Supervised Learning with Curriculum Pseudo Labeling](https://arxiv.org/abs/2110.08263)
- [FreeMatch: Self-adaptive Thresholding for Semi-supervised Learning](https://arxiv.org/abs/2205.07246)

<!-- /study-references -->

---

### 3. 생성 모델

#### 학습 목표

생성 모델의 확률적 목표와 연속·이산 잠재 표현을 익힌 뒤, DDPM·score·sampling·flow의 학습 신호와 생성 갱신을 먼저 설명한다. 이를 압축 공간의 조건부 생성·Transformer·비디오·조건 제어에 차례로 적용하고, 네트워크·학습 목표·조건·guidance·sampler의 역할과 품질·다양성·시간 일관성·계산 비용을 구분한다.

#### 학습 내용

#### 3-A. Generative Foundations

##### 19회차 · 날짜 미정 · 발표자: 미정 · VAE와 확률적 잠재변수

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| VAE | 생성 모델 | 필수 | **포함 개념:** Likelihood · Latent variable · Prior / Posterior · Encoder / Decoder · ELBO · Reconstruction / KL · Reparameterization<br>**확률적 모델:** 관측 이미지·잠재변수·우도의 관계, prior·실제 posterior·encoder의 근사 posterior 구분<br>**구조와 학습:** encoder가 예측하는 분포와 decoder의 조건부 분포, ELBO의 reconstruction·KL 항과 각 항의 역할<br>**Gradient 경로:** Gaussian latent의 평균·분산과 noise를 이용한 reparameterization, sampling을 거쳐 encoder까지 전달되는 gradient<br>**복원과 생성:** 입력 → posterior sample → 복원, prior sample → 새 이미지 생성의 차이와 재구성·분포 정규화의 균형 |

<!-- study-references:19 -->

- [Auto-Encoding Variational Bayes](https://arxiv.org/abs/1312.6114)

<!-- /study-references -->

##### 20회차 · 날짜 미정 · 발표자: 미정 · GAN과 adversarial learning

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| GAN | 생성 모델 | 중요 | **포함 개념:** Generator / Discriminator · Adversarial learning · Minimax / Non-saturating loss · Alternating updates · Mode collapse<br>**학습 신호:** noise → generator → 생성 이미지, 실제·생성 이미지를 판별하는 discriminator와 generator에 전달되는 신호<br>**목표와 갱신:** 원 minimax·non-saturating generator loss, 번갈아 학습할 때의 고정·갱신 파라미터와 gradient 경로<br>**학습과 추론:** 두 모델이 함께 바뀌는 최적화와 학습 불안정, 생성 시 generator를 사용하는 흐름<br>**결과 해석:** 개별 이미지 품질과 생성 분포의 다양성, mode collapse·데이터 분포의 일부만 생성하는 실패 사례 |

<!-- study-references:20 -->

- [Generative Adversarial Networks](https://arxiv.org/abs/1406.2661)
- [NIPS 2016 Tutorial: Generative Adversarial Networks](https://arxiv.org/abs/1701.00160)

<!-- /study-references -->

##### 21회차 · 날짜 미정 · 발표자: 미정 · Autoregressive 생성과 이산 image token

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Autoregressive Models | 생성 모델 | 중요 | **포함 개념:** Probability factorization · PixelCNN · Masked convolution · Next-pixel prediction · Teacher forcing · Sequential sampling<br>**확률 분해:** 앞선 픽셀·채널을 조건으로 다음 값을 예측하며 이미지의 확률을 구성하는 방식<br>**PixelCNN:** 예측할 정답과 픽셀·채널 순서, masked convolution으로 미래 정보를 차단하는 위치·연산<br>**학습과 생성:** 정답 문맥을 제공하는 teacher forcing·여러 위치의 loss 계산, 이미 생성한 값에 의존하는 순차 sampling과 비용<br>**앞뒤 연결:** 1장의 causal token prediction과 비교, 다음 VQ 계열의 이산 image token에 autoregressive prior를 적용하는 흐름 |
| VQ-VAE / VQGAN | 생성 모델 | 중요 | **포함 개념:** Encoder / Decoder · Codebook · Vector quantization · Straight-through estimator · Reconstruction / Codebook / Commitment loss · Perceptual / Adversarial loss · Token prior<br>**이산 표현:** encoder feature → 가까운 codebook 벡터 선택 → decoder, 공간 위치별 code index와 연속 feature의 차이<br>**VQ-VAE 학습:** reconstruction·codebook·commitment loss, stop-gradient·straight-through estimator와 파라미터별 gradient 경로<br>**VQGAN 비교:** quantized latent를 사용하는 tokenizer, perceptual·adversarial 목표와 discriminator가 복원에 주는 신호<br>**생성의 두 단계:** tokenizer 학습 → 고정한 tokenizer의 code index에 prior 학습, VQ-VAE의 PixelCNN·VQGAN의 Transformer prior 비교<br>**복원과 생성:** 입력 이미지의 code 복원과 새로운 code sampling 구분, 연속 latent VAE와의 표현·학습 목표 비교 |

<!-- study-references:21 -->

- [Pixel Recurrent Neural Networks](https://arxiv.org/abs/1601.06759)
- [Conditional Image Generation with PixelCNN Decoders](https://arxiv.org/abs/1606.05328)
- [Neural Discrete Representation Learning](https://arxiv.org/abs/1711.00937)
- [Taming Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2012.09841)

<!-- /study-references -->

#### 3-B. Diffusion & Flow Foundations

##### 22회차 · 날짜 미정 · 발표자: 미정 · DDPM: 노이즈 예측 학습과 반복 생성

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DDPM | 생성 모델 | 필수 | **포함 개념:** Forward noising · Noise schedule · Closed-form noisy sample · ε-prediction · Denoising MSE · Timestep embedding · U-Net / Skip connection · Reverse mean / Variance · Iterative sampling<br>**핵심 문제:** 순수 noise에서 이미지를 한 번에 만드는 대신, 여러 noise 수준에서 복원 방향을 학습해 반복 갱신하는 전체 과정을 설명<br>**학습 데이터와 target:** 정답 이미지 x_0·Gaussian noise ε·timestep t를 뽑아 x_t를 직접 만드는 식과 noise schedule을 확인. 매번 forward noising 전 단계를 실행할 필요가 없는 이유, network 입력·정답 noise·MSE를 연결<br>**Denoiser와 학습:** Noisy image·timestep embedding → U-Net → ε 예측의 shape와 gradient 경로를 추적. 해상도 축소·복원·skip connection은 network를 읽을 정도로 설명하고, ε 예측 목표를 먼저 완성<br>**생성 전체 흐름:** Gaussian 초기 noise → ε 예측 → 역방향 평균 계산 → 단계별 분산·추가 noise → 다음 sample을 끝까지 연결. 한 번의 학습 step과 한 번의 reverse update를 작은 예제로 계산<br>**학습 범위:** 22회차 안에서 학습과 noise-to-image 생성을 모두 완성. 학습 때만 쓰는 정답 이미지·noise와 생성 때 이용 가능한 입력을 구분하고, ELBO는 denoising 목표와의 관계까지 연결. 다른 출력 parameterization은 24회차에서 비교 |

<!-- study-references:22 -->

- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239)

<!-- /study-references -->

##### 23회차 · 날짜 미정 · 발표자: 미정 · Score-based Modeling: score와 연속 시간 생성

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Score-Based Modeling | 생성 모델 | 필수 | **포함 개념:** Score / Input log-density gradient · Denoising score matching · Noise-conditioned network · Score–ε relationship · Continuous time · Drift / Diffusion · Reverse-time SDE · Probability-flow ODE<br>**Score의 직관:** 주어진 noise 수준의 분포에서 입력을 어느 방향으로 움직이면 log-density가 증가하는지 나타내는 벡터. 입력에 대한 gradient와 network 파라미터 gradient를 구분<br>**학습 신호 연결:** Gaussian perturbation의 conditional score로 학습하는 denoising score matching과 DDPM의 ε 예측 사이의 noise scale·부호 관계를 확인<br>**SDE로 확장:** 이산 noising을 연속 시간의 drift·확률적 noise로 연결. Forward·reverse 시간 방향과 reverse-time SDE에서 학습한 score가 들어가는 항을 설명<br>**Probability-flow ODE:** 정확한 score를 가정하면 같은 시간별 marginal 분포를 따르는 결정적 ODE를 비교. 같은 분포와 같은 개별 궤적은 다르며 실제 모델 오차·수치 적분 오차도 구분<br>**학습 범위:** 식의 각 항·noise 유무·ε와 score의 연결을 읽는 데 집중. SDE 전체 이론·역시간 정리 증명은 확장 학습으로 두고, 다음 회차에서 실제 갱신을 계산 |

<!-- study-references:23 -->

- [Generative Modeling by Estimating Gradients of the Data Distribution](https://arxiv.org/abs/1907.05600)
- [Score-Based Generative Modeling through Stochastic Differential Equations](https://arxiv.org/abs/2011.13456)

<!-- /study-references -->

##### 24회차 · 날짜 미정 · 발표자: 미정 · Diffusion Sampling: 생성 갱신과 계산 비용

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Diffusion Sampling | 생성 방법 | 필수 | **포함 개념:** DDPM / DDIM updates · η · Timestep subsampling · ε / x_0 / v parameterization · Deterministic / Stochastic sampling · Euler / Heun · Discretization error · Steps / NFE · DPM-Solver<br>**학습 목표와 sampler:** Network가 예측하는 값·학습 loss와, 그 예측으로 다음 상태를 계산하는 sampler를 구분. DDPM reverse update를 기준으로 DDIM의 원본 추정·다음 sample 계산을 비교<br>**출력 parameterization:** 같은 noisy sample의 signal/noise 계수로 ε·x_0·v를 정의하고 출력 사이의 변환을 확인. v-parameterization과 25회차의 경로 미분인 flow velocity를 구분하며, 변환 가능성이 loss 가중치·학습 결과의 동일성을 뜻하지 않음을 설명<br>**DDIM과 시간 격자:** Timestep 부분집합과 학습 noise schedule의 차이, η에 따른 추가 noise·결정성을 확인. 같은 초기 noise에서 두세 번의 update를 비교<br>**ODE 계산:** Euler 한 번 갱신 → Heun의 방향 재평가·보정을 작은 예제로 계산. EDM의 sampler 설계와 DPM-Solver의 diffusion 전용 solver는 이 기본 원리 위의 확장으로 연결<br>**비용과 비교:** Step 수·network function evaluations(NFE)·단계 크기·이산화 오차를 구분. 같은 모델·조건·초기 noise·호출 예산에서 비교하고, distillation처럼 재학습하는 방법과 sampler만 바꾸는 방법의 차이를 확인<br>**학습 범위:** DDIM·Euler·Heun의 갱신과 비용 비교를 중심으로 다룸. 고차 solver 전체 유도·distillation 학습은 Related Work로 확장하고 Flow Matching의 ODE sampling으로 연결 |

<!-- study-references:24 -->

- [Denoising Diffusion Implicit Models](https://arxiv.org/abs/2010.02502)
- [Elucidating the Design Space of Diffusion-Based Generative Models](https://arxiv.org/abs/2206.00364)
- [Progressive Distillation for Fast Sampling of Diffusion Models](https://arxiv.org/abs/2202.00512)
- [DPM-Solver: A Fast ODE Solver for Diffusion Probabilistic Model Sampling in Around 10 Steps](https://arxiv.org/abs/2206.00927)

<!-- /study-references -->

##### 25회차 · 날짜 미정 · 발표자: 미정 · Flow Matching·Rectified Flow: 경로와 속도장 학습

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Flow Matching | 생성 방법 | 필수 | **포함 개념:** Probability path · Conditional path · Velocity field · Conditional flow matching · Velocity regression · ODE sampling · Time convention<br>**핵심 직관:** Noise 분포를 data 분포로 옮기는 경로를 정하고, 각 위치·시간에서 이동할 velocity를 학습. DDPM의 noise·score 예측과 학습 target·생성 갱신을 비교<br>**입력과 target:** Noise/data pair와 시간에서 conditional path의 위치·velocity target을 만들고 회귀 loss로 학습. 개별 pair의 조건부 경로와 전체 분포를 옮기는 field를 구분<br>**학습과 생성:** 학습용 위치·정답 velocity는 pair로 직접 계산하고, 생성은 초기 noise에서 학습한 field를 평가하며 ODE 적분. 여기서는 t=0 noise·t=1 data로 두고 앞 diffusion의 시간 방향과 비교<br>**연결 범위:** 24회차의 Euler·Heun을 같은 생성 갱신 원리로 적용. 경로 선택·학습 목표·network 구조·sampler가 서로 다른 설계 요소임을 확인하고, 일반 Flow Matching의 전체 이론은 확장 학습으로 연결 |
| Rectified Flow | 생성 방법 | 필수 | **포함 개념:** Coupling · Straight interpolation · Endpoint-difference target · Rectification / Reflow · Trajectory straightness · Few-step sampling<br>**직선 보간 예제:** Pair를 맺는 coupling을 정하고 noise·data의 직선 보간 위치와 두 끝점 차이인 velocity target을 계산. Flow Matching과 공통인 velocity 회귀·ODE sampling을 확인<br>**학습 경로와 생성 궤적:** 각 pair의 직선 학습 경로와 학습한 field의 실제 적분 궤적을 구분. 직선 target만으로 모든 생성 궤적·한 step 생성의 정확도가 보장되지는 않음을 설명<br>**Rectification과 reflow:** 학습한 ODE로 얻은 시작·끝 pair로 새 coupling을 만들고 다시 학습하는 흐름. 첫 학습과 reflow를 구분하고 궤적 직선성·이산화 오차·호출 수의 관계를 해석<br>**학습 깊이와 응용:** 직선 보간 target·한 번의 velocity 회귀·ODE 생성 흐름을 중심으로 다루고 reflow는 절차·효과를 비교. 다음 Latent Diffusion·MMDiT에서 표현 공간·조건·학습 목표를 분리해 연결 |

<!-- study-references:25 -->

- [Flow Matching for Generative Modeling](https://arxiv.org/abs/2210.02747)
- [Flow Straight and Fast: Learning to Generate and Transfer Data with Rectified Flow](https://arxiv.org/abs/2209.03003)
- [Flow Matching Guide and Code](https://arxiv.org/abs/2412.06264)

<!-- /study-references -->

#### 3-C. Conditional Image & Video Generation

##### 26회차 · 날짜 미정 · 발표자: 미정 · Latent Diffusion: 압축 공간의 조건부 생성

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Latent Diffusion | 생성 모델 | 필수 | **포함 개념:** Autoencoder · Latent compression · KL / VQ regularization · Frozen encoder / Decoder · Latent denoising · Text encoder · Noise latent / Image decoding<br>**왜 latent인가:** 픽셀 공간 대신 압축된 공간에서 반복 생성해 계산 비용을 줄이는 구조. 19·21회차의 autoencoder·연속/이산 표현과 연결하고 압축률·복원 품질의 균형을 확인<br>**학습의 두 단계:** 먼저 autoencoder의 이미지 → latent → 복원을 학습한 뒤 encoder·decoder를 고정하고 latent denoiser를 학습. KL/VQ regularization과 생성 network의 예측 target·loss를 구분<br>**전체 생성 흐름:** Text → text encoder, noise latent → 조건부 반복 갱신 → image decoder의 정보 흐름·shape·고정/학습 파라미터를 추적. Pixel-space DDPM과 바뀐 공간·유지되는 원리를 비교<br>**오차와 학습 범위:** Autoencoder 복원 한계와 생성 단계 오차를 구분. 원 LDM의 latent diffusion을 중심으로 설명하고, latent 공간 자체가 ε/score/flow 중 특정 학습 목표를 강제하는 것은 아니라는 점을 다음 MMDiT와 연결 |
| Conditioning & Guidance | 구성 요소 · 생성 방법 | 필수 | **포함 개념:** Class / Text conditioning · Cross-attention · FiLM / Feature modulation · AdaLN · Classifier guidance · Condition dropout · Classifier-free guidance / CFG · Guidance scale<br>**조건을 넣는 방식:** Noisy 상태·timestep·class/text 조건의 역할과 입력 위치를 구분. 이미지 feature의 Q와 text feature의 K·V를 결합하는 cross-attention을 1장에 연결<br>**Feature modulation:** 조건에서 만든 scale·shift를 적용하는 FiLM과 normalization 이후 조건별 affine 변환인 AdaLN의 적용 위치를 비교. AdaLN-Zero의 gate·초기화는 27회차에서 다룸<br>**Guidance의 원리:** Classifier guidance의 분류기 gradient는 score의 적용 사례로 짧게 비교. CFG는 condition dropout으로 조건부·무조건부 예측을 학습하고, 추론에서 두 예측을 guidance scale로 조합하는 흐름을 확인<br>**효과와 구분:** 조건 충실도·다양성·과도한 guidance의 영향과 두 예측의 호출 비용을 비교. 조건 입력 구조와 sampling 예측을 조절하는 guidance를 구분하고, ControlNet 같은 추가 조건 모듈은 29회차에서 연결 |

<!-- study-references:26 -->

- [High-Resolution Image Synthesis with Latent Diffusion Models](https://arxiv.org/abs/2112.10752)
- [Diffusion Models Beat GANs on Image Synthesis](https://arxiv.org/abs/2105.05233)
- [Classifier-Free Diffusion Guidance](https://arxiv.org/abs/2207.12598)
- [FiLM: Visual Reasoning with a General Conditioning Layer](https://arxiv.org/abs/1709.07871)

<!-- /study-references -->

##### 27회차 · 날짜 미정 · 발표자: 미정 · Diffusion Transformers: DiT·MMDiT

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DiT / MMDiT | 모델 · Denoiser | 필수 | **포함 개념:** Latent patch tokens · Timestep / Condition embeddings · AdaLN-Zero / Scale / Shift / Gate · DiT output head · Image / Text streams · Modality-specific weights · Joint attention · Diffusion / Rectified-flow targets<br>**구조의 변화:** 26회차의 압축 공간·조건부 생성에 1장의 Transformer를 적용. Latent → patch token → Transformer blocks → 공간 출력의 shape를 추적하고 U-Net의 해상도·skip 경로와 비교<br>**원 DiT:** Timestep·class embedding을 AdaLN-Zero의 scale·shift·gate로 전달하는 위치·초기화, ε·역방향 분산을 예측하는 output head와 원 diffusion 학습 목표를 확인<br>**MMDiT:** 이미지·텍스트별 가중치와 token stream → Q·K·V 결합의 joint attention → 각 stream 갱신의 흐름. LDM에서 이미지 query가 text feature를 읽는 cross-attention과 정보 교환 위치·방향을 비교<br>**구조와 목표:** DiT라는 network 구조와 ε/velocity 학습 target·sampling 방법을 분리. 원 DiT의 diffusion과 MMDiT의 rectified-flow 적용을 22–26회차 원리로 각각 설명<br>**학습 범위:** DiT 전체 흐름과 MMDiT의 결합 구조·목표 변화에 집중. Patch 크기·모델 규모·계산량의 ablation을 확인하고, 각 모델의 전체 재현은 확장 학습으로 두고, 비디오의 시간축 확장은 다음 회차로 연결 |

<!-- study-references:27 -->

- [Scalable Diffusion Models with Transformers](https://arxiv.org/abs/2212.09748)
- [Scaling Rectified Flow Transformers for High-Resolution Image Synthesis](https://arxiv.org/abs/2403.03206)

<!-- /study-references -->

##### 28회차 · 날짜 미정 · 발표자: 미정 · Video Generation: 시간축과 시공간 모델링

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Video Diffusion / Flow Models | 생성 모델 · 모델 구조 | 중요 | **포함 개념:** Video tensor / Frame axis · Spatial / Temporal attention · Temporal position · Motion module · Video latent / Spatiotemporal compression · Video patch tokens · Text-to-video / Image-to-video · Temporal consistency<br>**이미지에서 비디오로:** 이미지 batch와 여러 frame으로 된 clip을 구분하고 시간 축이 추가된 입력·noise·예측 target의 shape를 확인. Frame을 독립 생성할 때 정체성·외관·움직임이 일관되지 않는 문제를 설명<br>**시간 정보 결합:** Video Diffusion Models의 spatial/temporal attention을 기본 예제로 따라가고 frame 간 정보 전달·시간 위치 표현의 필요성을 확인. 작은 clip 예제로 spatial·temporal attention의 연산 축과 token 수를 추적<br>**이미지 모델의 확장:** AnimateDiff의 motion module과 고정 이미지 backbone의 정보 흐름을 주요 비교로 다룸. Stable Video Diffusion은 latent video·image conditioning의 사례로 연결하고 spatial/temporal 계산·고정/학습 범위를 비교<br>**Video Transformer로 연결:** CogVideoX의 시공간 압축 latent·video token·text 결합을 27회차와 비교. Wan은 추가 대표 사례로 연결하며 network 구조와 diffusion/flow 학습 target을 모델별로 구분<br>**조건과 비용:** Text-to-video·image-to-video의 조건 frame·text·noisy clip 입력 차이, 길이·해상도·압축률에 따른 token 수·메모리·sampling 비용을 비교. 카메라 이동과 객체 움직임을 구분해 다음 제어 회차로 연결<br>**학습 범위:** 시간 축·정보 결합을 중심으로 기본 video diffusion과 AnimateDiff를 설명하고 SVD·CogVideoX·Wan은 구조 변화 비교·Related Work로 확장. 모든 모델의 학습 recipe·전체 구현은 확장 학습으로 연결 |

<!-- study-references:28 -->

- [Video Diffusion Models](https://arxiv.org/abs/2204.03458)
- [AnimateDiff: Animate Your Personalized Text-to-Image Diffusion Models without Specific Tuning](https://arxiv.org/abs/2307.04725)
- [Stable Video Diffusion: Scaling Latent Video Diffusion Models to Large Datasets](https://arxiv.org/abs/2311.15127)
- [CogVideoX: Text-to-Video Diffusion Models with An Expert Transformer](https://arxiv.org/abs/2408.06072)
- [Wan: Open and Advanced Large-Scale Video Generative Models](https://arxiv.org/abs/2503.20314)

<!-- /study-references -->

##### 29회차 · 날짜 미정 · 발표자: 미정 · Controllable Generation: 이미지·비디오 조건 제어

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Controllable Image / Video Generation | 모델 · 조건 제어 | 중요 | **포함 개념:** ControlNet · Spatial conditions / Edge / Depth / Pose · Frozen backbone / Trainable branch · Zero convolution / Residual injection · IP-Adapter / Reference image / Decoupled cross-attention · SparseCtrl / Sparse condition frames · CameraCtrl / Camera pose / Ray encoding · Camera motion / Object motion<br>**제어 문제 구분:** 공간 구조·참조 이미지의 외관·일부 frame·카메라 경로가 무엇을 지정하는지 입력·출력으로 비교. Text 조건·sampling guidance·추가 조건 모듈의 역할을 나누고 CFG와 함께 쓸 수 있음을 확인<br>**ControlNet 중심 학습:** Edge/depth/pose → trainable branch → 여러 해상도 residual → 고정 backbone의 경로·shape를 추적. Zero-initialized convolution의 초기 출력·gradient 흐름·고정/학습 파라미터를 확인<br>**IP-Adapter 주요 비교:** 참조 이미지 feature를 별도 cross-attention 경로로 주입하는 방식과 ControlNet의 공간 조건 residual을 비교. T2I-Adapter는 조건 feature를 넣는 경량 adapter의 관련 사례로 연결<br>**비디오 제어로 확장:** SparseCtrl의 드문 condition frame·조건이 있는 위치 표시·시간축 정보 전달, CameraCtrl의 camera pose에서 만든 ray 조건과 video backbone 결합을 핵심 흐름으로 비교. 조건 frame 사이의 생성과 카메라/객체 motion을 구분<br>**관련 확장과 평가:** VideoComposer·MotionCtrl은 복합 조건·camera/object motion 제어, Prompt-to-Prompt·SDEdit은 편집의 관련 사례로 연결. 조건 일치도·시각 품질·시간 일관성을 분리하고 조건·seed·backbone을 맞춰 비교<br>**학습 범위:** ControlNet의 구조·학습·추론을 자세히, IP-Adapter를 주요 비교로 다루고 SparseCtrl·CameraCtrl은 28회차 위에서 새 조건의 입력·결합 위치를 비교. 역문제 복원·3D 최적화는 별도 응용으로 구분하며 이 회차의 공통 코어에 넣지 않음 |

<!-- study-references:29 -->

- [Adding Conditional Control to Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.05543)
- [T2I-Adapter: Learning Adapters to Dig out More Controllable Ability for Text-to-Image Diffusion Models](https://arxiv.org/abs/2302.08453)
- [IP-Adapter: Text Compatible Image Prompt Adapter for Text-to-Image Diffusion Models](https://arxiv.org/abs/2308.06721)
- [VideoComposer: Compositional Video Synthesis with Motion Controllability](https://arxiv.org/abs/2306.02018)
- [SparseCtrl: Adding Sparse Controls to Text-to-Video Diffusion Models](https://arxiv.org/abs/2311.16933)
- [MotionCtrl: A Unified and Flexible Motion Controller for Video Generation](https://arxiv.org/abs/2312.03641)
- [CameraCtrl: Enabling Camera Control for Text-to-Video Generation](https://arxiv.org/abs/2404.02101)
- [Prompt-to-Prompt Image Editing with Cross Attention Control](https://arxiv.org/abs/2208.01626)
- [SDEdit: Guided Image Synthesis and Editing with Stochastic Differential Equations](https://arxiv.org/abs/2108.01073)

<!-- /study-references -->
