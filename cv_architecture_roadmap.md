# CV 핵심 개념과 모델 스터디 계획

## 1. 운영계획

**주 1회, 회당 60분(방학 중에는 주 2회)** 동안 CV의 핵심 개념과 모델을 함께 공부합니다. **개념이 필요한 이유, 구조와 수식의 의미, 실제 동작 원리를 깊이 이해하는 것**을 목표로 합니다. 배운 내용을 자신의 언어와 구조도·수식·코드로 설명하고, 연구에서 설계와 활용을 판단하는 데 연결합니다.

### 1. 세션 준비와 진행

담당자는 아래 여섯 단계에 따라 내용을 준비하고, 세션도 같은 순서로 진행합니다. 목표는 개념이 필요한 이유와 작동 원리를 이해하고, 그 효과와 한계, 연구에서의 활용까지 연결하는 것입니다.

기준 논문이 있는 주제는 해당 논문을 출발점으로 삼습니다. 그 외에는 여러 논문·교재·강의·공식 문서·코드를 참고해 설명을 구성합니다. 각 단계를 펼쳐 세부 준비 안내를 확인할 수 있습니다.

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
| **5분** | 40–45분 | 5. Related Work · 관련 연구와 발전 흐름 | 다른 연구에서는 어떻게 이어지고 달라졌는가? | **자료 선정:** 주제 이해에 도움이 되는 대표 자료·후속 연구 2–3개<br>**발전 흐름:** 유지·변형·대체된 원리와 구조<br>**핵심 차이:** 최근 활용 방식·접근별 차이·참고 자료 |
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

<!-- point-example:resnet label:ResNet -->

주제: **Residual learning의 필요성과 shortcut의 작동 원리**

- [ ] **1. 왜 층을 더 쌓는 것만으로는 충분하지 않을까요?** 더 깊은 네트워크가 학습 데이터조차 더 잘 맞추지 못할 수 있는 이유와, residual learning이 해결하려는 문제를 설명해 보세요.
- [ ] **2. Residual block은 입력을 어떻게 출력으로 바꾸나요?** 입력 `x`가 지나는 두 경로를 그리고, `F(x)`가 무엇을 학습하는지와 shortcut이 어떻게 결합되는지 수식으로 나타내 보세요.
- [ ] **3. Shortcut은 학습에 어떤 경로를 더하나요?** shortcut을 제거한 경우와 비교해, 정보와 gradient가 전달되는 흐름이 어떻게 달라지는지 설명해 보세요.
- [ ] **4. 덧셈을 다른 결합 방식으로 바꿔도 같은 구조일까요?** 덧셈과 concatenation을 비교해 출력 차원과 residual learning의 의미가 어떻게 달라지는지 설명해 보세요.

참고자료: [Deep Residual Learning for Image Recognition — 원문](https://arxiv.org/pdf/1512.03385), §1·§3.1–3.3, Figure 2·3 및 Eq. (1)–(2).
<!-- /point-example -->

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

신경망 기초부터 생성 모델까지 0–4장의 학습 항목을 정리합니다. 각 모델의 구조·수식·학습·구현을 함께 살펴보며, 원리가 밀접하게 연결된 후속 모델은 주요 변화를 비교합니다.


### 개념 유형 구분

학습 항목 옆의 유형은 해당 항목의 성격과 세션에서 중점적으로 다루는 역할을 나타냅니다. 둘 이상의 관점으로 다루면 **모델 · 학습 방법**처럼 함께 표기합니다.

| 유형 | 의미 | 예시 |
|---|---|---|
| 기초 개념 | 텐서 표현과 layer의 동작, 초기화 등 모델 이해의 바탕 | Tensor / Linear / MLP, Activation / Initialization |
| 기초 연산 | 모델을 구성하는 기본 계산과 변환 | Convolution / Pooling, Normalization |
| 학습 원리 | 오차를 정의하고 gradient를 계산하는 원리 | Loss / Backpropagation / Autograd |
| 학습 방법 | 학습 신호·목표·업데이트·전이 방식을 정하는 방법 | Optimization, Regularization, SimCLR, DINO, MAE |
| 모델 구조 | 여러 모델에서 활용하는 블록 구성과 정보 흐름 | Transformer |
| 모델 | 구조와 학습 목표를 특정 작업에 맞게 구성한 전체 | U-Net, CLIP, DETR, DPT, SAM |
| 구성 요소 | 모델 안에서 feature 결합 등 특정 역할을 맡는 구조 | FPN |
| 구현 기법 | 계산 목표를 유지하며 연산·메모리 사용·실행 흐름을 효율화하는 기법 | FlashAttention, KV cache |
| 적응 방법 | 사전학습 모델을 새로운 작업이나 데이터 분포에 맞게 조정하는 기법 | LoRA |
| 분석 방법 | 학습 상태·데이터·모델의 표현과 특성을 관찰하고 평가하는 방법 | 모델 진단, PCA, t-SNE, UMAP |
| 추정 방법 | 관측값에서 잔차와 이상치를 고려해 모델의 파라미터를 구하는 방법 | Least Squares, RANSAC |
| 생성 모델 | 데이터 분포를 학습해 새 샘플을 만드는 모델 계열과 시스템 | VAE, GAN, DDPM, Latent Diffusion |
| 생성 방법 | 생성 경로·sampling 절차 또는 이를 위한 학습 목표를 정의하는 방법 | DDIM, Flow Matching, Rectified Flow |

**Backbone·Neck·Denoiser·조건 제어**는 모델이나 구성 요소의 역할을 덧붙이는 표기입니다. 각각 feature 추출, 다중 해상도 feature 결합, 노이즈 제거를 위한 예측, 조건 입력 반영을 뜻합니다. 예를 들어 ResNet은 **모델 · Backbone**, FPN은 **구성 요소 · Neck**, DiT는 **모델 · Denoiser**, ControlNet은 **모델 · 조건 제어**로 표시합니다.

유형과 함께 구조·학습 목표·데이터·학습과 추론의 흐름을 살펴보고, 설계의 효과와 한계를 설명할 수 있는 것을 목표로 합니다.

---

### 0. 신경망 기초와 실험·분석 도구

#### 학습 목표

신경망의 연산·미분·파라미터 갱신과 학습 안정성·일반화의 원리를 설명한다. 실험 설계·모델 진단·표현 분석·추정 도구를 활용해 학습·분석 결과의 신뢰성과 한계를 해석한다.

#### 학습 내용

#### 0-A. Neural Network Basics

입력 표현부터 예측·미분·파라미터 갱신·일반화와 실제 훈련 기법까지, 아래 일곱 항목으로 정리합니다. 각 항목을 펼치면 포함 개념과 세부 학습 내용을 확인할 수 있습니다. 포함 개념은 해당 항목에서 실제로 설명하고 이해할 범위입니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Tensor / Linear / MLP | 기초 개념 | 필수 | **포함 개념:** Tensor shape · Batch / Channel / Spatial / Token axes · Reshape / Transpose · Matrix multiplication · Broadcasting · Linear layer · Parameter count · MLP<br>**텐서와 연산:** 축의 의미, reshape·transpose 전후 shape, 행렬 곱·broadcasting의 조건<br>**Linear layer:** 입력·출력 차원, 가중치·bias의 역할, 파라미터 수와 batch 내 가중치 공유<br>**MLP 구성:** Linear와 activation의 조합, 입력 → 은닉 표현 → logits의 수식·코드 연결 |
| Activation / Initialization | 기초 개념 | 필수 | **포함 개념:** Nonlinearity · ReLU · GELU · SiLU · Sigmoid / Tanh · Saturation · Xavier initialization · He initialization · Vanishing / Exploding gradients<br>**비선형성:** activation의 필요성, 함수별 출력·gradient와 saturation, activation 제거 시의 변화<br>**초기화:** 가중치 크기·대칭성이 activation·gradient에 미치는 영향, Xavier·He의 가정과 적용 대상<br>**직접 확인:** 초기화 크기에 따른 층별 출력·gradient 분포, 소실·폭주가 나타나는 조건 |
| Loss / Backpropagation / Autograd | 학습 원리 | 필수 | **포함 개념:** Logits / Probability / Target · Cross-entropy · MSE · Computational graph · Chain rule · Backpropagation · Autograd · .grad accumulation / Reset · zero_grad / backward / step<br>**예측과 오차:** logits·확률·target 구분, 분류의 cross-entropy와 회귀의 MSE, loss와 정확도의 차이<br>**미분과 갱신:** 계산 그래프·chain rule로 gradient 계산, backpropagation과 optimizer의 역할 구분<br>**코드 연결:** 작은 forward·backward와 Autograd 비교, 반복된 backward의 .grad 누적과 zero_grad 초기화, backward의 미분·step의 갱신 구분, CrossEntropyLoss의 softmax 전 logits 입력 |
| Optimization / LR Scheduling | 학습 방법 | 필수 | **포함 개념:** Full-batch / Stochastic / Mini-batch GD · SGD · Momentum · Adam · AdamW · Learning rate · Warmup · Step decay · Cosine decay · L2 penalty · Weight decay<br>**Gradient 계산 단위:** full-batch·stochastic·mini-batch의 사용 데이터·갱신 빈도·gradient 변동 비교<br>**파라미터 갱신:** SGD·Momentum·Adam·AdamW의 갱신식·상태 변수, 학습률과 갱신 크기<br>**학습률 조정:** warmup·step·cosine schedule의 목적과 변화 방식, 학습 곡선·안정성과의 관계<br>**Weight decay:** L2 penalty와 파라미터 감쇠의 관계, Adam의 L2 regularization과 AdamW의 decoupled weight decay 차이 |
| Normalization | 기초 연산 | 필수 | **포함 개념:** BatchNorm (BN) · LayerNorm (LN) · GroupNorm (GN) · RMSNorm · Normalization axes · Mean / Variance / RMS · Scale / Bias · Running statistics · Training / Evaluation modes<br>**정규화 축:** BN·LN·GN·RMSNorm의 계산 대상, 평균·분산·RMS와 batch 의존성<br>**학습과 추론:** 기본 BN의 batch 통계·누적 통계, LN·GN·RMSNorm의 입력 기반 통계, 방식별 scale·bias 적용 차이<br>**구조 연결:** 정규화의 배치와 선택 이유, 초기화와 정규화가 개입하는 시점·역할의 차이 |
| Regularization | 학습 방법 | 필수 | **포함 개념:** Generalization · Overfitting / Underfitting · Training / Validation gap · Dropout · Weight decay · Data augmentation · Mixup · CutMix<br>**일반화:** 학습·검증 곡선, 과적합·과소적합 구분, regularization 강도와 성능의 관계<br>**모델·파라미터:** dropout의 mask·스케일 조정·학습/추론 차이, weight decay 강도에 따른 파라미터 크기·학습/검증 성능 변화. 갱신식은 Optimization과 연결<br>**데이터 증강:** 증강의 가정, Mixup의 입력·label 혼합, CutMix의 영역 교체·면적 비례 label 혼합 |
| Training Techniques | 학습 방법 | 중요 | **포함 개념:** Exponential Moving Average (EMA) · Gradient norm / Value clipping · Automatic Mixed Precision (AMP) · FP16 / BF16 · Autocast · Gradient scaling<br>**EMA:** 파라미터의 지수이동평균, 현재 가중치·평균 가중치 구분, 평가용 평균과 teacher 갱신의 목적 차이<br>**Gradient clipping:** norm·value 기반 clipping, gradient 크기·갱신에 미치는 영향, gradient scaling 사용 시 unscale 이후 clipping<br>**Mixed precision:** 연산별 정밀도 선택, autocast와 FP16 gradient scaling의 역할, 메모리·계산 비용·수치 안정성 |

#### 0-B. Experiments & Analysis

학습 결과를 신뢰할 수 있는지, 어떤 표현이 만들어졌는지, 관측에 모델이 얼마나 잘 맞는지 살펴봅니다. 각 도구는 ResNet·표현 학습·기하 등 관련 주제와 연결해 반복 활용합니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Experiments & Diagnostics | 분석 방법 | 필수 | **포함 개념:** Train / Validation / Test split · Data leakage · Random seed · Baseline · Ablation · Learning curves · Feature maps · Activation / Weight / Gradient statistics · Failure cases<br>**실험 설계:** 데이터 분할·누수 방지, 비교 대상·변경 요소·고정 조건, seed·반복 실험과 결과 변동<br>**학습 진단:** loss·평가 지표·학습/검증 곡선, 층별 activation·weight·gradient 분포, 과적합·학습 불안정의 구분<br>**모델 분석:** 동일 입력의 층별 반응·특징맵·학습 전후 변화, 실패 사례와 구조 변경의 영향, 관찰과 해석의 구분 |
| SVD / PCA / Low-Rank Approximation | 기초 연산 · 분석 방법 | 필수 | **포함 개념:** Singular Value Decomposition (SVD) · U / Σ / Vᵀ · Singular values · Rank · Low-rank approximation · Data centering · Principal Component Analysis (PCA) · Explained variance · Projection / Reconstruction<br>**분해와 rank:** SVD 각 행렬의 역할·차원, singular value와 주요 방향, rank를 줄일 때의 근사·복원 오차<br>**PCA:** 중심화한 feature 행렬의 SVD, 주성분 방향·설명 분산, 저차원 투영·복원<br>**실제 활용:** feature 압축·주요 변화 방향 분석, 선형 최소제곱·기하적 정렬로의 확장, 저랭크 개념과 LoRA의 연결 |
| Embedding Analysis | 분석 방법 | 중요 | **포함 개념:** Feature / Embedding · L2 normalization · Cosine / Euclidean distance · PCA baseline · t-SNE · Perplexity · UMAP · n_neighbors / min_dist · k-NN · Linear probing<br>**표현과 거리:** 분석할 layer·feature 선택, 정규화·거리 정의, 같은 샘플의 학습 전후·모델 간 비교<br>**차원 축소:** PCA를 기준으로 t-SNE·UMAP의 이웃 관계와 저차원 배치 비교, t-SNE의 perplexity·UMAP의 n_neighbors와 min_dist·seed에 따른 시각화 변화<br>**해석과 평가:** 2D 군집 크기·거리·분리의 왜곡 가능성, 원래 feature 공간의 이웃 검색·linear probe로 함께 확인 |
| Least Squares / RANSAC | 추정 방법 | 중요 | **포함 개념:** Least squares · Residual · Noise / Outlier · Inlier · Minimal sample · Model hypothesis · Consensus · Residual threshold · Max trials / Confidence · Inlier refit<br>**최소제곱:** 관측·모델·파라미터·잔차의 관계, 잔차 제곱합 최소화, 노이즈·이상치에 대한 민감성<br>**RANSAC:** 표본 추출 → 모델 추정 → inlier 판정 → 후보 비교·재추정, 최소 표본 크기·inlier 비율·목표 confidence에 따른 반복 횟수, residual threshold가 inlier 판정·재추정에 미치는 영향<br>**실제 활용:** 이상치가 섞인 직선 피팅으로 시작, feature matching·homography·점군 모델 추정으로 확장, 모델·잔차 정의에 따른 적용 조건 |

### 1. CNN과 비전 모델

#### 학습 목표

Convolution·residual learning·encoder–decoder·다중 해상도 feature의 동작과 역할을 설명한다. 검출·분할 모델을 출력·정답 할당·loss·추론 후처리 관점에서 비교하고, 구조별 설계 이유와 계산 비용을 해석한다.

#### 학습 내용

아래 다섯 항목은 개념에 따른 학습 묶음입니다. 각 항목의 분량과 이해의 깊이에 따라 회차를 나눌 수 있습니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Convolution / Pooling | 기초 연산 | 필수 | **포함 개념:** Locality / Weight sharing · Kernel / Stride / Padding / Dilation · Output shape · Receptive field · 1×1 / Group / Depthwise convolution · Parameter count / Computation cost · Max / Average / Global average pooling<br>**필요성:** 이미지의 공간 구조를 활용하는 지역 연결·가중치 공유, 완전 연결 연산과의 차이<br>**공간 연산:** kernel·stride·padding·dilation에 따른 출력 shape·receptive field 계산<br>**연산 비용:** 일반·1×1·group·depthwise convolution의 채널 연결, 파라미터 수·연산량 비교<br>**Pooling:** max·average·global average pooling의 출력, 해상도·정보 손실과 분류 head의 연결 |
| ResNet / Residual Learning | 모델 · Backbone | 필수 | **포함 개념:** Degradation · Residual learning · Identity / Projection shortcut · Basic block / Bottleneck · Stage · Gradient flow · Pre-activation<br>**필요성:** 깊어진 plain network에서 학습 오차까지 커지는 degradation 문제, residual learning의 접근<br>**잔차와 shortcut:** F(x) + x의 의미, residual branch가 학습하는 함수와 identity 경로의 역할<br>**블록과 stage:** basic block·bottleneck, 해상도·채널 변화, identity·projection shortcut의 조건과 gradient 흐름<br>**설계 근거:** shortcut ablation, 원 ResNet과 후속 pre-activation 변형의 차이 |
| Encoder–Decoder / Multi-Scale Features | 모델 · 구성 요소 | 필수 | **포함 개념:** Semantic / Instance / Panoptic segmentation · U-Net · Encoder–Decoder · Skip connection / Concatenation · Up-convolution / Crop · FPN · Top-down pathway / Lateral connection · Feature pyramid / Addition<br>**과제 구분:** semantic은 픽셀별 범주, instance는 개별 객체의 mask, panoptic은 모든 픽셀의 범주와 셀 수 있는 객체의 개체 구분을 함께 예측<br>**U-Net · 분할 모델:** 문맥을 얻는 encoder와 위치 정보를 복원하는 decoder, encoder feature의 concatenation과 shape 변화<br>**U-Net 해상도 정렬:** 원 논문의 up-convolution·crop, interpolation 등 후속 구현과의 차이<br>**FPN · Neck:** backbone의 여러 stage → top-down upsampling·lateral 1×1 convolution·addition → 다중 해상도 feature, 결합 전 해상도·채널 정렬<br>**함께 비교:** U-Net의 픽셀별 출력과 FPN의 feature 출력, concatenation·addition의 차이, ResNet shortcut과 각 연결의 목적 비교 |
| Object Detection | 모델 | 필수 | **포함 개념:** Bounding box / Class prediction · Faster R-CNN · RPN / Anchor box / Proposal · RoIPool · Objectness · Box regression · YOLOX · One-stage / Two-stage · Anchor-based / Anchor-free · Multi-scale features · Decoupled head · SimOTA / Dynamic-k assignment · Classification / Objectness / Box loss · IoU / NMS · AP / Latency<br>**문제와 출력:** 여러 객체의 위치·종류 예측, box 좌표 표현·IoU, 분류·objectness·위치 오차의 학습 신호<br>**Faster R-CNN:** 공유 backbone → RPN의 proposal 생성 → RoIPool → 분류·box 보정, anchor·proposal의 정답 할당과 각 loss<br>**YOLOX 구조:** backbone·다중 스케일 neck → 분리된 분류·위치 추정 head, anchor box 없이 grid 위치와 box offset을 이용하는 예측·좌표 변환<br>**YOLOX 학습:** SimOTA의 후보 영역·분류/위치 비용·dynamic-k 양성 예측 선택·중복 할당 해결, 선택 결과에 따른 class·objectness·box loss<br>**학습과 추론:** 정답 할당과 NMS의 역할 구분, YOLOX의 anchor-free 예측에서도 필요한 NMS, Faster R-CNN의 proposal 선택·후처리와 비교<br>**평가와 근거:** AP50·AP@[.5:.95]의 차이, 입력 해상도·장치·batch·정밀도·후처리 포함 여부를 맞춘 latency 비교, YOLOX의 head·anchor-free·정답 할당 ablation |
| Instance Segmentation | 모델 | 중요 | **포함 개념:** Mask R-CNN · Instance mask · RoIPool / RoIAlign · Coordinate quantization · Bilinear sampling · Mask branch / Target · Pixel-wise binary loss · Multi-task learning<br>**필요성:** 객체별 bounding box만으로 표현하기 어려운 경계·형상, semantic segmentation과의 출력 차이<br>**Mask R-CNN 구조:** Faster R-CNN의 분류·box 예측과 병렬로 추가한 mask branch, 검출에서 분할로의 확장<br>**공간 정렬:** RoIPool의 좌표 양자화 문제, RoIAlign의 bilinear sampling과 위치 정보 보존<br>**Mask 학습·추론:** RoI별 mask target·픽셀별 binary loss, 분류·box loss와의 결합, 추론 시 예측 class에 해당하는 mask 선택<br>**설계 근거:** 원 논문의 RoIAlign·mask branch 관련 ablation과 효과가 확인된 조건 |

### 2. Transformer와 비전·멀티모달 모델

#### 학습 목표

Attention·위치 표현·Transformer의 계산 흐름과 비전·멀티모달 모델의 정보 결합 구조를 설명한다. 과제별 출력·학습 목표·추론 방식을 비교하고, 연산·메모리 효율화 기법의 적용 조건과 비용을 해석한다.

#### 학습 내용

#### 2-A. Transformer Foundations

아래 다섯 항목으로 공통 원리와 비전 backbone을 공부합니다. 각 항목은 학습 묶음이며, 분량과 이해의 깊이에 따라 회차를 나눌 수 있습니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Attention | 기초 연산 | 필수 | **포함 개념:** Query / Key / Value · Scaled dot-product attention · Softmax axis · Self-attention / Cross-attention · Multi-head attention · Causal / Padding mask · Tensor shape / Computation cost · Permutation equivariance / Position information<br>**필요성:** 토큰마다 필요한 문맥을 다른 토큰에서 가져오는 방식, 입력에 따라 달라지는 정보 결합<br>**계산 흐름:** Q·K·V의 생성과 shape → QKᵀ·√d_k 스케일링 → mask·softmax → V의 가중합, 작은 입력 예제의 값·차원 추적<br>**정보의 출처:** self-attention과 cross-attention에서 Q·K·V를 가져오는 입력, query·key 길이가 다를 때의 출력 shape<br>**Head와 mask:** head별 projection·결합, softmax 정규화 축, causal·padding mask가 허용하는 정보 범위<br>**계산 비용:** 토큰 수에 따른 attention 행렬의 크기·연산량·메모리 사용 변화<br>**위치 정보로 연결:** 위치 정보와 순서 의존 mask가 없을 때 self-attention의 permutation equivariance, 토큰의 내용과 함께 순서·공간 배치를 전달해야 하는 이유 |
| Transformer Architecture | 모델 구조 | 필수 | **포함 개념:** Token embedding · Sinusoidal positional encoding · Encoder / Decoder · FFN · Residual connection · LayerNorm / RMSNorm · Pre-Norm / Post-Norm · GPT / BERT · Next-token prediction · Masked language modeling · Training / Generation<br>**입력과 기본 위치 표현:** token embedding에 sinusoidal positional encoding을 더하는 원 Transformer의 입력, 두 벡터의 차원·역할과 encoder·decoder에 들어가는 위치. 고정된 위치 표현과 학습하는 위치 embedding의 차이<br>**전체 구조:** 위치 정보가 포함된 입력 → encoder의 self-attention·FFN → decoder의 causal self-attention·cross-attention·FFN → 출력, residual·normalization의 연결<br>**블록 변형:** Pre-Norm·Post-Norm의 연산 순서와 gradient 경로, 0장에서 배운 LayerNorm·RMSNorm의 역할을 연결해 비교<br>**GPT 비교 사례:** decoder-only 구조와 causal self-attention, 한 칸 이동한 입력·target의 next-token prediction과 loss<br>**BERT 비교 사례:** encoder-only 구조와 양방향 self-attention, token·segment·position embedding, 가린 token을 맞히는 MLM 입력·target·loss 위치<br>**학습과 활용:** GPT의 학습 시 병렬 계산·자기회귀 생성, BERT의 입력 문맥과 downstream head. GPT·BERT는 구조·정보 범위·학습 목표 비교에 집중하고 세대별 전체 재현은 심화로 확장 |
| Positional Encoding Variants | 구성 요소 | 중요 | **포함 개념:** Learned absolute position · Relative position bias · RoPE · Embedding / Attention score / Q–K injection · 1D / 2D position · Sequence length / Resolution change<br>**비교 출발점:** 02에서 배운 sinusoidal encoding을 기준으로, 위치 정보를 입력 embedding·attention score·Q/K 중 어디에 반영하는지 비교<br>**Learned absolute position:** 위치별 embedding의 학습, 고정된 sinusoidal encoding과의 차이, 학습 범위를 벗어난 길이·해상도의 처리<br>**Relative position bias:** 토큰 간 상대적 거리·방향을 attention score에 반영하는 방식, 상대 위치와 절대 위치의 구분<br>**RoPE:** Q·K에 적용하는 위치별 회전, 두 토큰의 상대 위치가 내적에 반영되는 방식과 적용 지점<br>**비전으로 확장:** 1D 문장 위치와 2D 이미지 위치, ViT·Swin에서의 선택과 해상도·window 크기 변화에 따른 처리 |
| ViT / Swin Transformer | 모델 · Backbone | 필수 | **포함 개념:** ViT · Patch embedding · CLS token / Readout · Learned positional embedding · Global attention · Swin Transformer · Window / Shifted-window attention · Patch merging · Relative position bias · Multi-scale features<br>**ViT:** 이미지 → patch·Linear projection → CLS·위치 embedding → encoder → 분류 출력, 단계별 token 수·shape 추적<br>**ViT 출력·해상도:** 원 모델의 CLS 기반 분류, 해상도 변경 시 위치 embedding 보간, pooling 등 readout 변형과의 차이<br>**Swin:** window 내부 attention과 shifted window의 정보 교환, patch merging에 따른 해상도·채널 변화와 상대 위치 bias<br>**비전 backbone 비교:** ViT의 전역 attention·일정한 token 해상도, Swin·CNN의 계층적 feature, dense prediction에 전달하는 출력<br>**설계 근거:** 국소성·계층 구조 등 inductive bias, 데이터 규모·사전학습·입력 해상도에 따른 성능·계산 비용의 변화 |
| Efficient Attention / KV Cache | 구현 기법 | 중요 | **포함 개념:** Attention computation / Memory cost · FlashAttention · Tiling / Online softmax · GPU memory IO · KV cache · Autoregressive generation · Prefill / Decode · Memory–Computation trade-off<br>**비용의 출처:** projection·attention score·가중합의 연산, 토큰 수에 따른 N×N 행렬과 중간 결과 저장 비용<br>**FlashAttention:** tiling·online softmax로 attention의 수학적 계산을 유지하며 GPU 메모리 이동·중간 행렬 저장을 줄이는 원리. Dense attention의 연산량은 토큰 수에 대해 여전히 이차적으로 증가<br>**KV cache:** 자기회귀 생성에서 이전 토큰의 K·V를 저장·재사용하는 조건, prefill과 토큰별 decode, 층별 cache의 shape·메모리 증가<br>**적용 범위 비교:** FlashAttention의 학습·추론 계산과 KV cache의 생성 시 재사용, 계산 절감·메모리 사용의 교환 관계<br>**학습 깊이:** 작은 예제로 cache 유무의 계산 흐름·메모리 사용 비교, GPU kernel 구현과 세부 최적화는 선택 심화 |

#### 2-B. Vision & Multimodal Models

1장의 검출·분할과 연결해 출력 구조를 비교합니다. VLM에서는 이미지·언어의 연결 구조를 먼저 이해하고, CLIP 등 표현 학습의 원리는 3장에서 이어서 공부합니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DETR / End-to-End Detection | 모델 | 필수 | **포함 개념:** DETR · Set prediction · Object query · CNN backbone / Transformer encoder–decoder · Bipartite / Hungarian matching · Matching cost / Training loss · No-object class · Bounding box prediction · NMS-free inference · YOLOv10 · One-to-many / One-to-one heads · Consistent matching metric · Top-one assignment<br>**필요성:** 객체의 순서가 정해지지 않은 정답 집합, 예측 중복과 정답 할당을 함께 다루는 set prediction<br>**DETR 구조:** CNN feature·위치 정보 → encoder → learned object query를 사용하는 decoder → 고정 개수의 class·box 예측<br>**DETR 학습:** Hungarian matching의 비용과 matching 후 계산하는 class·box loss의 차이, unmatched query의 no-object 처리<br>**YOLOv10 비교:** 학습 시 one-to-many·one-to-one head를 함께 사용하고, 추론 시 one-to-one head로 예측하는 흐름. 풍부한 학습 신호와 중복 예측 억제의 역할 분담<br>**할당 방식 비교:** YOLOv10의 class score·IoU 기반 일관된 matching metric과 top-one 선택, DETR의 Hungarian matching과 다른 계산 방식<br>**1장과 연결:** Faster R-CNN·YOLOX의 proposal·밀집 예측·정답 할당·NMS와 비교, anchor-free 여부와 NMS-free 여부를 구분. YOLOv10의 비교 범위는 두 head·할당·loss·추론 경로 |
| Dense Prediction / DPT | 모델 | 필수 | **포함 개념:** Dense prediction · Depth / Semantic segmentation · ViT / Hybrid backbone · Intermediate tokens · Reassemble · Spatial feature map · Multi-resolution fusion · Convolutional decoder<br>**필요성:** 이미지 단위 표현에서 픽셀별 깊이·범주 출력으로의 전환, 문맥과 공간 위치를 함께 보존하는 decoder의 역할<br>**DPT 동작:** backbone의 여러 층에서 얻은 token → 공간 feature 재배열·해상도 변환 → convolutional decoder의 점진적 fusion → 픽셀별 출력<br>**학습과 출력:** 깊이 추정·semantic segmentation의 target·출력 채널·loss 차이, backbone과 task별 head의 연결<br>**1장·backbone과 비교:** vanilla ViT의 중간 층이 처음부터 해상도 pyramid인 것은 아니라는 점, Swin·FPN·U-Net의 feature·복원 경로와 차이 |
| Promptable Segmentation / SAM | 모델 | 중요 | **포함 개념:** SAM · Image encoder · Prompt encoder · Point / Box / Mask prompt · Mask decoder · Cross-attention · Multiple masks / Quality prediction · Image embedding reuse · SAM 2 / Streaming memory<br>**필요성:** 점·박스·mask 지시에 따라 달라지는 분할 대상, 고정된 범주 예측과 prompt 기반 분할의 차이<br>**원 SAM 구조:** image encoder·prompt encoder·mask decoder, 이미지·prompt 표현의 정보 교환과 mask 생성<br>**학습·추론:** 데이터·prompt sampling·mask loss, 모호한 prompt에 대한 복수 mask·품질 예측, 같은 이미지에 대한 embedding 재사용<br>**SAM 2 비교:** streaming memory와 프레임별 prompt·mask 처리, 이미지 분할에서 비디오 처리로 확장하며 추가된 정보 흐름<br>**학습 범위:** 원 SAM의 구조·학습·추론을 중심으로 후속 변화를 비교하고, 버전별 전체 구조·평가는 선택 심화 |
| VLM / Visual Tokens | 모델 | 중요 | **포함 개념:** LLaVA · Vision encoder · Projector · LLM · Visual tokens · Image–Text token sequence · Feature alignment / Instruction tuning · Frozen / Trainable parameters · Next-token loss · Autoregressive response generation<br>**필요성:** 이미지 표현과 언어 모델의 token 표현 연결, 시각 정보가 질문의 문맥과 응답에 반영되는 경로<br>**원 LLaVA 구조:** 사전학습 vision encoder → linear projector → visual token, 텍스트 token과 함께 LLM에 입력되는 위치·shape와 응답 생성<br>**두 단계 학습:** feature alignment에서 projector 학습, instruction tuning에서 projector·LLM 학습. 두 단계 모두 vision encoder 고정, 단계별 데이터·target·gradient 경로 비교<br>**학습과 생성:** 정답 응답 위치의 next-token loss, 학습 시 제공되는 응답과 생성 시 이전 token을 이용하는 흐름의 차이<br>**3장과 연결:** CLIP의 이미지–텍스트 표현 정렬과 VLM의 응답 생성 목적 구분, 사전학습·전이·fine-tuning의 원리와 근거 |

### 3. 표현 학습과 모델 적응

#### 학습 목표

대조·복원·teacher–student 학습에서 표현을 만드는 학습 신호와 target 생성 방식을 설명한다. 사전학습 표현의 평가·전이·조정 방법을 비교하고, 라벨 가용성·분포 변화·데이터 접근 조건에 맞춰 결과를 해석한다.

#### 학습 내용

아래 여덟 항목으로 표현 학습부터 전이·데이터 활용·분포 변화까지 연결합니다. 포함 개념은 해당 항목에서 실제로 설명하고 이해할 범위이며, 분량과 이해의 깊이에 따라 회차를 나눌 수 있습니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Pretraining & Transfer | 학습 방법 · 적응 방법 | 필수 | **포함 개념:** Pretraining / Downstream task · Supervised / Self-supervised pretraining · Backbone / Head · Frozen features · Linear probing · Partial / Full fine-tuning · LoRA · Low-rank update / Rank / Scale · Initialization · Parameter freezing / Gradient flow · Trainable parameter count · Pretraining data / Evaluation protocol<br>**학습 단계:** 사전학습 → 표현 평가 → 새 작업으로 전이, 단계별 데이터·target·head 변화와 표현의 재사용<br>**평가와 조정:** linear probing·부분/전체 fine-tuning의 고정·갱신 파라미터와 gradient 경로, 표현 자체의 품질과 추가 학습 후 성능 구분<br>**LoRA:** 고정한 가중치에 ΔW = BA를 더하는 저랭크 변화량 학습, 적용 위치·행렬 차원·rank·scale·초기화·gradient 경로·학습 파라미터 수 비교<br>**실험 해석:** 사전학습 목표·데이터·backbone·학습 조건을 맞춘 평가, 사전학습 데이터와 평가 데이터의 중복·누수 확인 |
| Contrastive Learning | 학습 방법 | 필수 | **포함 개념:** SimCLR · Positive / Negative pairs · Data augmentation · Encoder / Projection head · Normalized embeddings · NT-Xent loss · Temperature · Batch size · Representation / Projection · Linear evaluation<br>**학습 목표:** 같은 이미지의 두 증강을 연결하고 다른 이미지의 표현과 구별하는 목표, 증강으로 무시할 변화와 보존할 정보<br>**계산과 loss:** 두 증강 → encoder → projection → 정규화·유사도 → NT-Xent, positive·negative 쌍과 temperature가 gradient에 미치는 영향<br>**학습 후 활용:** loss에 쓰는 projection과 downstream task의 representation 구분, encoder feature의 linear evaluation<br>**설계 근거:** 증강·batch 크기·projection head의 영향을 ablation으로 확인, 학습 목표와 평가 조건의 연결 |
| Image–Text Alignment | 모델 · 학습 방법 | 필수 | **포함 개념:** CLIP · SigLIP · Image / Text encoders · Paired image–text data · Normalized embeddings · Similarity matrix · Bidirectional softmax loss · Pairwise sigmoid loss · Temperature / Scale / Bias · Zero-shot classification<br>**학습 목표:** 이미지와 텍스트를 비교 가능한 공간에 정렬, 언어로 시각 개념을 지정하는 방식<br>**CLIP:** 두 encoder → 정규화된 embedding → batch 내 유사도 행렬, 정답 쌍·오답 쌍과 양방향 softmax loss<br>**SigLIP 비교:** pair별 일치 여부를 학습하는 sigmoid loss, CLIP의 softmax 정규화와 다른 target·loss 구성, scale·bias의 역할<br>**Zero-shot 추론:** class prompt → text embedding → 이미지와의 유사도 → 분류, 학습한 task head를 쓰는 분류와의 차이<br>**2장과 연결:** VLM의 응답 생성과 표현 정렬의 목적 비교, batch·pair 구성·데이터·평가 조건에 따른 결과 해석 |
| Masked Image Modeling | 학습 방법 | 필수 | **포함 개념:** MAE · Patch masking · Visible-token encoder · Mask token · Positional information · Asymmetric encoder–decoder · Pixel reconstruction · Masked-region loss · Downstream transfer<br>**학습 목표:** 가린 부분의 복원으로 문맥·표현을 학습하는 이유, 복원 품질과 downstream 성능의 구분<br>**MAE 구조:** 보이는 patch만 encoder에 입력 → 원래 위치로 배치·mask token 추가 → decoder → pixel 복원, 위치 정보·단계별 shape 추적<br>**Target과 loss:** 가린 영역의 pixel target·복원 오차, masking 비율·비대칭 구조와 계산량의 관계<br>**학습 후 활용:** 복원용 decoder와 downstream head의 역할 구분, encoder 전이·표현 평가와 설계 ablation |
| Knowledge Distillation | 학습 방법 | 필수 | **포함 개념:** Teacher / Student · Logits / Soft targets · Temperature · Cross-entropy / KL divergence · Soft-target / Hard-label losses · Frozen teacher · Student gradients<br>**전달할 정보:** 정답 class 외에 teacher의 출력 분포가 전달하는 정보, 모델 압축·지식 전이의 목적<br>**학습 경로:** 고정 teacher의 target 생성과 student 업데이트, teacher 출력을 실제 정답과 구분<br>**Temperature와 loss:** temperature에 따른 분포 변화, soft-target·hard-label loss의 결합·가중치·스케일과 cross-entropy·KL의 관계<br>**근거와 한계:** teacher 예측 오류·모델 용량·데이터 조건과 student 성능의 관계, 다음 DINO의 teacher·target 생성 방식과 비교 |
| Self-Distillation | 학습 방법 | 필수 | **포함 개념:** DINO / DINOv2 / DINOv3 · Teacher / Student · Multi-crop · EMA teacher · Stop-gradient · Cross-entropy · Centering / Sharpening · Collapse · Image / Masked-patch objectives · Gram anchoring · Global / Dense feature evaluation<br>**원 DINO:** 같은 이미지의 서로 다른 crop → teacher 출력 분포 → student의 cross-entropy 학습, class label 없이 target을 만드는 방식<br>**Teacher와 안정화:** 원 DINO의 EMA teacher·stop-gradient, global·local crop의 대응, centering·temperature sharpening과 collapse 방지<br>**DINOv2 비교:** 이미지 수준·가린 patch 수준 학습 목표, teacher가 제공하는 target과 student 입력·loss 위치. MAE의 pixel 복원과 다른 학습 신호<br>**DINOv3 비교:** 정규화한 patch feature의 쌍별 내적으로 만드는 Gram matrix, 이전 teacher에서 얻은 기준 관계에 맞추는 anchoring loss와 밀집 특징의 일관성<br>**평가와 비교 범위:** 버전별 target·loss·teacher 역할, 전역 표현·밀집 특징 품질 비교. 후속 버전은 명시한 학습 목표·특징 관계를 중심으로 이해 |
| Semi-Supervised Learning | 학습 방법 | 중요 | **포함 개념:** Labeled / Unlabeled data · FixMatch · Pseudo-labels · Confidence threshold · Weak / Strong augmentation · Consistency regularization · Supervised / Unsupervised losses · Stop-gradient<br>**문제 상황:** 일부에만 정답이 있을 때 나머지 데이터를 활용하는 방법, 실제 label과 예측으로 만든 target의 구분<br>**FixMatch 흐름:** 약한 증강의 예측 → confidence threshold → pseudo-label → 강한 증강의 학습 target, consistency의 의미<br>**Loss와 gradient:** 정답 데이터·정답 없는 데이터의 loss 결합, pseudo-label의 stop-gradient와 학습에서 제외되는 샘플<br>**실패 조건·평가:** 잘못된 정답의 반복 학습·class 불균형·확신도 오판, 실제 label 수·unlabeled data 접근 조건을 맞춘 평가 |
| Domain Shift & Generalization | 기초 개념 | 중요 | **포함 개념:** Source / Target domains · Distribution shift · Dataset bias · Synthetic-to-real · Domain adaptation / Generalization · Target data / Labels · Evaluation protocol<br>**문제 상황:** 같은 작업에서 카메라·조명·데이터 출처가 달라질 때의 성능 변화, 합성·실제 데이터 사이의 분포 차이<br>**문제 설정:** target 데이터로 조정하는 adaptation과 target별 추가 조정 없이 평가하는 generalization, source·target의 데이터·label 가용성<br>**평가 조건:** 학습·조정·평가에 사용한 데이터와 label의 접근 범위, 평가 데이터 누수와 target별 추가 학습 여부<br>**결과 해석:** 분포 변화에 대한 일반화와 target 데이터 사용 효과 구분, 분포가 달라진 요인·실패 사례·비교 조건 확인 |

---

### 4. 생성 모델

#### 학습 목표

생성 모델의 확률적 목표와 연속·이산 잠재 표현, noise·score·velocity의 학습 신호를 설명한다. 네트워크·조건 입력·sampling의 역할을 구분하고, 구조와 생성 절차에 따른 품질·다양성·계산 비용을 해석한다.

#### 학습 내용

생성 원리·표현을 다루는 4-A와 Diffusion·Flow를 다루는 4-B로 구성합니다. 포함 개념은 해당 항목에서 실제로 설명하고 이해할 범위이며, 분량과 이해의 깊이에 따라 회차를 나눌 수 있습니다.

#### 4-A. Generative Foundations

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| VAE | 생성 모델 | 필수 | **포함 개념:** Likelihood · Latent variable · Prior / Posterior · Encoder / Decoder · ELBO · Reconstruction / KL · Reparameterization<br>**확률적 모델:** 관측 이미지·잠재변수·우도의 관계, prior·실제 posterior·encoder의 근사 posterior 구분<br>**구조와 학습:** encoder가 예측하는 분포와 decoder의 조건부 분포, ELBO의 reconstruction·KL 항과 각 항의 역할<br>**Gradient 경로:** Gaussian latent의 평균·분산과 noise를 이용한 reparameterization, sampling을 거쳐 encoder까지 전달되는 gradient<br>**복원과 생성:** 입력 → posterior sample → 복원, prior sample → 새 이미지 생성의 차이와 재구성·분포 정규화의 균형 |
| GAN | 생성 모델 | 중요 | **포함 개념:** Generator / Discriminator · Adversarial learning · Minimax / Non-saturating loss · Alternating updates · Mode collapse<br>**학습 신호:** noise → generator → 생성 이미지, 실제·생성 이미지를 판별하는 discriminator와 generator에 전달되는 신호<br>**목표와 갱신:** 원 minimax·non-saturating generator loss, 번갈아 학습할 때의 고정·갱신 파라미터와 gradient 경로<br>**학습과 추론:** 두 모델이 함께 바뀌는 최적화와 학습 불안정, 생성 시 generator를 사용하는 흐름<br>**결과 해석:** 개별 이미지 품질과 생성 분포의 다양성, mode collapse·데이터 분포의 일부만 생성하는 실패 사례 |
| Autoregressive Models | 생성 모델 | 중요 | **포함 개념:** Probability factorization · PixelCNN · Masked convolution · Next-pixel prediction · Teacher forcing · Sequential sampling<br>**확률 분해:** 앞선 픽셀·채널을 조건으로 다음 값을 예측하며 이미지의 확률을 구성하는 방식<br>**PixelCNN:** 예측할 정답과 픽셀·채널 순서, masked convolution으로 미래 정보를 차단하는 위치·연산<br>**학습과 생성:** 정답 문맥을 제공하는 teacher forcing·여러 위치의 loss 계산, 이미 생성한 값에 의존하는 순차 sampling과 비용<br>**앞뒤 연결:** 2장의 causal token prediction과 비교, 다음 VQ 계열의 이산 image token에 autoregressive prior를 적용하는 흐름 |
| VQ-VAE / VQGAN | 생성 모델 | 중요 | **포함 개념:** Encoder / Decoder · Codebook · Vector quantization · Straight-through estimator · Reconstruction / Codebook / Commitment loss · Perceptual / Adversarial loss · Token prior<br>**이산 표현:** encoder feature → 가까운 codebook 벡터 선택 → decoder, 공간 위치별 code index와 연속 feature의 차이<br>**VQ-VAE 학습:** reconstruction·codebook·commitment loss, stop-gradient·straight-through estimator와 파라미터별 gradient 경로<br>**VQGAN 비교:** quantized latent를 사용하는 tokenizer, perceptual·adversarial 목표와 discriminator가 복원에 주는 신호<br>**생성의 두 단계:** tokenizer 학습 → 고정한 tokenizer의 code index에 prior 학습, VQ-VAE의 PixelCNN·VQGAN의 Transformer prior 비교<br>**복원과 생성:** 입력 이미지의 code 복원과 새로운 code sampling 구분, 연속 latent VAE와의 표현·학습 목표 비교 |

#### 4-B. Diffusion & Flow

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DDPM | 생성 모델 | 필수 | **포함 개념:** Forward noising · Noise schedule · Closed-form noisy sample · ε-prediction · Denoising loss · Timestep embedding · U-Net · Reverse sampling<br>**Forward와 target:** 이미지에 Gaussian noise를 더하는 과정, noise schedule과 임의 timestep의 noisy sample을 바로 만드는 식, 정답 noise 생성<br>**구조와 학습:** noisy 입력·timestep embedding → U-Net → ε 예측, 학습에서 사용하는 이미지·noise·timestep과 denoising loss<br>**Reverse sampling:** 예측 noise로 역방향 평균을 계산하는 과정, 분산·추가 noise의 역할과 반복 갱신<br>**학습과 생성:** 정답 이미지에서 학습용 입력을 만드는 과정과 noise에서 이미지를 생성하는 과정, 학습 target·추론 시 이용 가능한 정보 구분 |
| Score-Based Modeling | 생성 모델 | 필수 | **포함 개념:** Score · Denoising score matching · Noise-conditioned network · Score–ε relationship · Reverse-time SDE · Probability-flow ODE<br>**Score의 의미:** 입력에 대한 log-density의 gradient, noise 수준에 따라 달라지는 데이터 분포와 score 방향<br>**학습 신호:** Gaussian perturbation의 conditional score를 이용한 denoising score matching, noise-conditioned network와 ε 예측의 관계<br>**연속 시간 관점:** forward·reverse-time SDE의 시간 방향·drift·noise 항, 역과정에서 학습한 score를 사용하는 위치<br>**Probability-flow ODE:** 정확한 score를 가정할 때 SDE와 같은 시간별 분포를 따르는 결정적 과정, 분포와 개별 궤적의 차이<br>**이해 범위:** 각 식의 항·noise 유무·학습 신호와 생성 과정의 연결, 다음 Sampling에서 작은 예제의 갱신 계산 |
| Diffusion Sampling | 생성 방법 | 필수 | **포함 개념:** DDIM · η · Timestep subsampling · Deterministic / Stochastic updates · Euler / Heun · Discretization error · NFE<br>**학습과 sampling:** 학습한 denoiser를 활용하며 생성 갱신식을 바꾸는 DDIM, timestep 부분집합과 학습 noise schedule의 구분<br>**DDIM 갱신:** 현재 noisy sample → 원본 추정 → 다음 sample, η에 따른 추가 noise와 같은 초기 noise에서의 결정성<br>**ODE 계산:** Euler의 한 번 갱신과 Heun의 기울기 재평가·보정, 작은 예제로 이동 방향·다음 상태 비교<br>**비용과 오차:** 단계 크기·이산화 오차·품질의 관계, step 수와 network function evaluations(NFE)의 차이<br>**비교 조건:** 같은 모델·초기 noise·조건·호출 예산에서 sampler·시간 격자 비교, 이후 Flow Matching·Rectified Flow의 ODE sampling과 연결 |
| Conditioning & Guidance | 구성 요소 · 생성 방법 | 필수 | **포함 개념:** Class / Text conditioning · Cross-attention · Feature modulation / FiLM · AdaLN · Condition dropout · Classifier-free guidance<br>**조건 입력:** class·text 표현을 생성 네트워크에 전달하는 위치, noisy 입력·시간 정보·조건 정보의 역할 구분<br>**Cross-attention:** 이미지 feature에서 Q, 조건 token에서 K·V를 만드는 정보 결합과 tensor shape, 2장의 attention 원리 적용<br>**Feature modulation:** 조건으로 만든 scale·shift를 feature에 적용하는 FiLM, normalization 뒤의 조건별 affine 변환인 AdaLN과 연산 위치 비교<br>**CFG 학습·추론:** condition dropout으로 조건부·무조건부 예측을 학습, 두 예측을 guidance scale로 조합하는 갱신 신호<br>**효과와 비용:** 조건 반영 강도·다양성·과도한 guidance의 영향, 조건부·무조건부 평가의 계산 비용과 뒤 모델들의 적용 위치 |
| Latent Diffusion | 생성 모델 | 필수 | **포함 개념:** Autoencoder · Latent compression · Autoencoder regularization · Frozen encoder / Decoder · Latent denoising · Text conditioning<br>**압축 단계:** 먼저 학습한 autoencoder의 이미지 → latent → 복원, 압축률·복원 품질과 KL·VQ regularization의 차이<br>**생성 학습:** 고정한 autoencoder로 latent를 만들고 denoiser 학습, pixel 공간과 latent 공간의 입력·target·계산 비용 비교<br>**조건과 추론:** text encoder·cross-attention·CFG의 적용 위치, noise latent → 반복 denoising → image decoder의 전체 흐름<br>**표현의 한계:** autoencoder의 복원 손실과 생성 단계의 오차 구분, 연속·이산 latent와 prior를 4-A의 VAE·VQ 계열에 연결 |
| ControlNet | 모델 · 조건 제어 | 중요 | **포함 개념:** Spatial conditions · Frozen backbone · Trainable branch · Zero convolution · Multi-scale residual injection<br>**공간 조건:** edge·depth·pose 등의 공간 배치와 text 조건의 차이, 조건 image가 추가 branch에 들어가는 경로<br>**구조와 연결:** 사전학습 backbone 고정·trainable branch 구성, 여러 해상도에서 조건 residual을 추가하는 위치·shape<br>**초기화와 학습:** zero-initialized convolution의 초기 출력, 원 모델의 출력을 유지하며 조건 신호를 추가하는 과정과 gradient 흐름<br>**추론과 근거:** 조건 입력·강도가 결과에 미치는 영향, 고정·학습 파라미터와 구조 ablation을 3장의 전이·조정 원리와 연결 |
| Flow Matching | 생성 방법 | 필수 | **포함 개념:** Probability path · Conditional path · Velocity field · Velocity regression · ODE sampling<br>**분포의 이동:** noise 분포와 data 분포를 잇는 probability path, 시간별 sample을 이동시키는 velocity field의 역할<br>**학습 target:** conditional path에서 시간별 위치·velocity target 생성, network가 예측한 velocity와의 회귀 loss<br>**생성 과정:** 초기 noise → 학습한 field 평가 → ODE 적분 → sample, 학습용 conditional path와 실제 생성 궤적의 구분<br>**비교와 연결:** DDPM의 ε·score와 다른 예측 대상, 경로·시간 방향·sampler의 역할, 다음 Rectified Flow의 직선 보간 목표와 비교 |
| Rectified Flow | 생성 방법 | 필수 | **포함 개념:** Coupling · Straight interpolation · Velocity target · Rectification / Reflow · Trajectory straightness<br>**Pair와 target:** 두 분포의 sample을 연결하는 coupling, 직선 보간 위의 입력과 두 끝점 차이로 만드는 velocity target<br>**학습과 궤적:** velocity 회귀와 학습한 field의 ODE 적분, 학습에 사용한 직선 보간과 생성 궤적이 달라지는 이유<br>**Rectification과 reflow:** 적분으로 얻은 끝점 pair로 새 coupling을 만들고 다시 학습하는 과정, 초기 pair와 생성 pair의 출처 구분<br>**속도와 정확도:** 궤적의 직선성·이산화 오차·sampling 단계 수의 관계, 적은 단계에서의 품질을 실제로 비교<br>**Flow Matching과 비교:** 공통인 velocity 학습과 ODE sampling을 바탕으로, coupling·직선 보간·reflow의 역할을 구분 |
| DiT / MMDiT | 모델 | 필수 | **포함 개념:** Latent patch tokens · Timestep / Condition embeddings · AdaLN-Zero · DiT output head · Image / Text streams · Modality-specific weights · Joint attention<br>**원 DiT 구조:** latent → patch token → Transformer blocks → 출력 복원, timestep·class embedding과 단계별 shape<br>**조건과 출력:** AdaLN-Zero의 scale·shift·gate와 초기화, ε·역방향 분산을 예측하는 원 DiT output head와 학습 목표<br>**MMDiT 구조:** 이미지·텍스트별 가중치와 token stream, Q·K·V를 결합하는 joint attention 뒤 각 stream으로 정보를 나누는 흐름<br>**학습 목표 비교:** 원 DiT의 diffusion 학습과 MMDiT의 rectified-flow 적용, 생성 네트워크 구조·예측 target·sampling 방법의 구분<br>**설계 근거:** U-Net·DiT·MMDiT의 정보 결합, patch 크기·모델 규모·계산량과 성능, 앞서 배운 latent·조건·flow 원리로 전체 구조 설명 |
