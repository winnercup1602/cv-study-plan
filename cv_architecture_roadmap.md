# CV 핵심 개념과 모델 스터디 계획

## 1. 운영계획

**주 1회, 회당 60분(방학 중에는 주 2회)** 동안 CV의 핵심 개념과 모델을 함께 공부합니다. **개념이 필요한 이유, 구조와 수식의 의미, 실제 동작 원리를 깊이 이해하는 것**을 목표로 합니다. 배운 내용을 자신의 언어와 구조도·수식·코드로 설명하고, 연구에서 설계와 활용을 판단하는 데 연결합니다.

매 세션은 **이전 내용 복습·학습 포인트 제시 → Why → What → How → Evidence → 관련 연구와 발전 흐름 → 한계와 연구 활용 → 학습 포인트 확인·공유 기록** 순서로 진행합니다. 현장에서 공유 기록의 초안을 남기고, 세션 후 근거와 표현을 보완해 한 페이지로 완성합니다.

### 1. 학습 Level

| Level | 도달 기준 | 적용 기준 |
|---|---|---|
| **L1 · 직관** | 개념이 필요한 이유와 해결하는 문제를 이해하고, 핵심 아이디어를 자신의 언어와 쉬운 예·figure로 설명할 수 있습니다. | 모든 구성원의 공통 목표 |
| **L2 · 동작 원리** | 입력부터 출력까지의 계산 흐름, 구성요소·중요 수식의 역할과 가정, 학습·추론의 차이와 설계 이유를 설명할 수 있습니다. | 모든 구성원의 기본 도달 기준 |
| **L3 · 연구와 구현** | 수식·구현 수준에서 동작을 추적하고, 설계의 근거·한계·대안과 조건이 바뀔 때의 영향을 분석할 수 있습니다. | 담당자의 준비 기준. 구성원은 자신의 연구와 연결되는 부분부터 심화 |

**필수 / 중요는 학습 우선순위**, **L1 / L2 / L3는 이해의 깊이**를 나타냅니다. 구성원은 L1–L2를 공통 목표로 삼고, 담당자는 동작 원리를 수식·구현과 연결하며 설계 근거·한계·대안까지 준비합니다.

### 2. 세션 준비와 진행

담당자는 아래 여섯 단계에 따라 내용을 준비하고, 세션도 같은 순서로 진행합니다. 목표는 개념이 필요한 이유와 작동 원리를 이해하고, 그 효과와 한계, 연구에서의 활용까지 연결하는 것입니다.

기준 논문이 있는 주제는 해당 논문을 출발점으로 삼습니다. 그 외에는 여러 논문·교재·강의·공식 문서·코드를 참고해 설명을 구성합니다. 각 단계를 펼쳐 세부 준비 안내를 확인할 수 있습니다.

#### 시작 점검 · **5분** (0–5분)

| 소요 시간 | 진행 구간 | 단계 | 중심 질문 | 세부 안내 |
|---|---|---|---|---|
| **5분** | 0–5분 | 이전 내용 복습 + 학습 포인트 제시 | 지난 내용과 이번 학습 목표는 무엇인가? | **이전 복습:** 지난 공유 기록의 학습 포인트·수정한 설명·남은 질문. 첫 세션은 선수 개념 점검<br>**이번 제시:** 주제·목표 Level·학습 포인트<br>**사전 준비:** 시작·종료에 같은 문장·항목·순서의 작성지, 설명·수식·도식 작성 공간, 인원수에 맞춰 출력 |

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

### 3. 학습 포인트 확인

**시작에 안내한 학습 포인트를 같은 문장·항목·순서로 다시 확인합니다.**

1. **각자 작성 · 5분.** 자료나 다른 사람의 답을 보지 않고, 인쇄된 작성지의 모든 항목에 설명·수식·도식으로 답합니다. 막힌 부분도 표시합니다.
2. **함께 확인·기록 · 5분.** 답의 주요 차이와 오해를 확인하고, 수정한 설명·남은 질문·근거 위치를 공유 기록의 초안으로 남깁니다. 세션 후 보완해 다음 복습의 기준으로 사용합니다.

작성지에는 항목별로 **내 설명·수식·도식 / 막힌 부분·남은 질문** 공간을 둡니다.

<!-- point-example:resnet label:ResNet -->

주제: **Residual learning의 필요성과 shortcut의 작동 원리** · 목표: **L2**

- [ ] **1. 왜 층을 더 쌓는 것만으로는 충분하지 않을까요?** 더 깊은 네트워크가 학습 데이터조차 더 잘 맞추지 못할 수 있는 이유와, residual learning이 해결하려는 문제를 설명해 보세요.
- [ ] **2. Residual block은 입력을 어떻게 출력으로 바꾸나요?** 입력 `x`가 지나는 두 경로를 그리고, `F(x)`가 무엇을 학습하는지와 shortcut이 어떻게 결합되는지 수식으로 나타내 보세요.
- [ ] **3. Shortcut은 학습에 어떤 경로를 더하나요?** shortcut을 제거한 경우와 비교해, 정보와 gradient가 전달되는 흐름이 어떻게 달라지는지 설명해 보세요.
- [ ] **4. 덧셈을 다른 결합 방식으로 바꿔도 같은 구조일까요?** 덧셈과 concatenation을 비교해 출력 차원과 residual learning의 의미가 어떻게 달라지는지 설명해 보세요.

참고자료: [Deep Residual Learning for Image Recognition — 원문](https://arxiv.org/pdf/1512.03385), §1·§3.1–3.3, Figure 2·3 및 Eq. (1)–(2).
<!-- /point-example -->

<!-- point-example:transformer label:Transformer -->

주제: **토큰 사이의 정보 교환과 encoder–decoder의 작동 원리** · 목표: **L2**

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
| 적응 방법 | 사전학습 모델을 새로운 작업에 맞게 조정하는 기법 | LoRA |
| 분석 방법 | 학습 상태·데이터·모델의 표현과 특성을 관찰하고 평가하는 방법 | 모델 진단, PCA, t-SNE, UMAP |
| 추정 방법 | 관측값에서 잔차와 이상치를 고려해 모델의 파라미터를 구하는 방법 | Least Squares, RANSAC |
| 생성 모델 | 데이터 분포를 학습해 새 샘플을 만드는 모델 계열과 시스템 | VAE, GAN, DDPM, Latent Diffusion |
| 생성 방법 | 생성 경로·sampling 절차 또는 이를 위한 학습 목표를 정의하는 방법 | DDIM, Flow Matching, Rectified Flow |

**Backbone·Neck·Denoiser·조건 제어**는 모델이나 구성 요소의 역할을 덧붙이는 표기입니다. 각각 feature 추출, 다중 해상도 feature 결합, 노이즈 제거를 위한 예측, 조건 입력 반영을 뜻합니다. 예를 들어 ResNet은 **모델 · Backbone**, FPN은 **구성 요소 · Neck**, DiT는 **모델 · Denoiser**, ControlNet은 **모델 · 조건 제어**로 표시합니다.

유형과 함께 구조·학습 목표·데이터·학습과 추론의 흐름을 살펴보고, 설계의 효과와 한계를 설명할 수 있는 것을 목표로 합니다.

---

### 0. 신경망 기초와 실험·분석 도구

#### 학습 목표

텐서 연산과 학습 과정의 원리를 이해하고, 실험 설계·모델 진단·표현 분석·피팅 도구로 학습 결과와 한계를 해석한다.

#### 학습 내용

#### 0-A. 신경망 연산과 학습 기초

입력 표현부터 예측·미분·파라미터 갱신·일반화와 실제 훈련 기법까지, 아래 일곱 항목으로 정리합니다. 각 항목을 펼치면 포함 개념과 세부 학습 내용을 확인할 수 있습니다. 포함 개념은 해당 항목에서 실제로 설명하고 이해할 범위입니다.

| 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Tensor / Linear / MLP | 기초 개념 | 필수 | **포함 개념:** Tensor shape · Batch / Channel / Spatial / Token axes · Reshape / Transpose · Matrix multiplication · Broadcasting · Linear layer · Parameter count · MLP<br>**텐서와 연산:** 축의 의미, reshape·transpose 전후 shape, 행렬 곱·broadcasting의 조건<br>**Linear layer:** 입력·출력 차원, 가중치·bias의 역할, 파라미터 수와 batch 내 가중치 공유<br>**MLP 구성:** Linear와 activation의 조합, 입력 → 은닉 표현 → logits의 수식·코드 연결 |
| Activation / Initialization | 기초 개념 | 필수 | **포함 개념:** Nonlinearity · ReLU · GELU · SiLU · Sigmoid / Tanh · Saturation · Xavier initialization · He initialization · Vanishing / Exploding gradients<br>**비선형성:** activation의 필요성, 함수별 출력·gradient와 saturation, activation 제거 시의 변화<br>**초기화:** 가중치 크기·대칭성이 activation·gradient에 미치는 영향, Xavier·He의 가정과 적용 대상<br>**직접 확인:** 초기화 크기에 따른 층별 출력·gradient 분포, 소실·폭주가 나타나는 조건 |
| Loss / Backpropagation / Autograd | 학습 원리 | 필수 | **포함 개념:** Logits / Probability / Target · Cross-entropy · MSE · Computational graph · Chain rule · Backpropagation · Autograd · .grad accumulation / Reset · zero_grad / backward / step<br>**예측과 오차:** logits·확률·target 구분, 분류의 cross-entropy와 회귀의 MSE, loss와 정확도의 차이<br>**미분과 갱신:** 계산 그래프·chain rule로 gradient 계산, backpropagation과 optimizer의 역할 구분<br>**코드 연결:** 작은 forward·backward와 Autograd 비교, 반복된 backward의 .grad 누적과 zero_grad 초기화, backward의 미분·step의 갱신 구분, CrossEntropyLoss의 softmax 전 logits 입력 |
| Optimization / Learning-rate scheduling | 학습 방법 | 필수 | **포함 개념:** Full-batch / Stochastic / Mini-batch GD · SGD · Momentum · Adam · AdamW · Learning rate · Warmup · Step decay · Cosine decay · L2 penalty · Weight decay<br>**Gradient 계산 단위:** full-batch·stochastic·mini-batch의 사용 데이터·갱신 빈도·gradient 변동 비교<br>**파라미터 갱신:** SGD·Momentum·Adam·AdamW의 갱신식·상태 변수, 학습률과 갱신 크기<br>**학습률 조정:** warmup·step·cosine schedule의 목적과 변화 방식, 학습 곡선·안정성과의 관계<br>**Weight decay:** L2 penalty와 파라미터 감쇠의 관계, Adam의 L2 regularization과 AdamW의 decoupled weight decay 차이 |
| Normalization | 기초 연산 | 필수 | **포함 개념:** BatchNorm (BN) · LayerNorm (LN) · GroupNorm (GN) · RMSNorm · Normalization axes · Mean / Variance / RMS · Scale / Bias · Running statistics · Training / Evaluation modes<br>**정규화 축:** BN·LN·GN·RMSNorm의 계산 대상, 평균·분산·RMS와 batch 의존성<br>**학습과 추론:** 기본 BN의 batch 통계·누적 통계, LN·GN·RMSNorm의 입력 기반 통계, 방식별 scale·bias 적용 차이<br>**구조 연결:** 정규화의 배치와 선택 이유, 초기화와 정규화가 개입하는 시점·역할의 차이 |
| Regularization | 학습 방법 | 필수 | **포함 개념:** Generalization · Overfitting / Underfitting · Training / Validation gap · Dropout · Weight decay · Data augmentation · Mixup · CutMix<br>**일반화:** 학습·검증 곡선, 과적합·과소적합 구분, regularization 강도와 성능의 관계<br>**모델·파라미터:** dropout의 mask·스케일 조정·학습/추론 차이, weight decay 강도에 따른 파라미터 크기·학습/검증 성능 변화. 갱신식은 Optimization과 연결<br>**데이터 증강:** 증강의 가정, Mixup의 입력·label 혼합, CutMix의 영역 교체·면적 비례 label 혼합 |
| Training Techniques | 학습 방법 | 중요 | **포함 개념:** Exponential Moving Average (EMA) · Gradient norm / Value clipping · Automatic Mixed Precision (AMP) · FP16 / BF16 · Autocast · Gradient scaling<br>**EMA:** 파라미터의 지수이동평균, 현재 가중치·평균 가중치 구분, 평가용 평균과 teacher 갱신의 목적 차이<br>**Gradient clipping:** norm·value 기반 clipping, gradient 크기·갱신에 미치는 영향, gradient scaling 사용 시 unscale 이후 clipping<br>**Mixed precision:** 연산별 정밀도 선택, autocast와 FP16 gradient scaling의 역할, 메모리·계산 비용·수치 안정성 |

#### 0-B. 실험 설계와 모델·데이터 분석 도구

학습 결과를 신뢰할 수 있는지, 어떤 표현이 만들어졌는지, 관측에 모델이 얼마나 잘 맞는지 살펴봅니다. 각 도구는 ResNet·표현 학습·기하 등 관련 주제와 연결해 반복 활용합니다.

| 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| 실험 설계와 모델 진단 | 분석 방법 | 필수 | **포함 개념:** Train / Validation / Test split · Data leakage · Random seed · Baseline · Ablation · Learning curves · Feature maps · Activation / Weight / Gradient statistics · Failure cases<br>**실험 설계:** 데이터 분할·누수 방지, 비교 대상·변경 요소·고정 조건, seed·반복 실험과 결과 변동<br>**학습 진단:** loss·평가 지표·학습/검증 곡선, 층별 activation·weight·gradient 분포, 과적합·학습 불안정의 구분<br>**모델 분석:** 동일 입력의 층별 반응·특징맵·학습 전후 변화, 실패 사례와 구조 변경의 영향, 관찰과 해석의 구분 |
| SVD / PCA / Low-rank approximation | 기초 연산 · 분석 방법 | 필수 | **포함 개념:** Singular Value Decomposition (SVD) · U / Σ / Vᵀ · Singular values · Rank · Low-rank approximation · Data centering · Principal Component Analysis (PCA) · Explained variance · Projection / Reconstruction<br>**분해와 rank:** SVD 각 행렬의 역할·차원, singular value와 주요 방향, rank를 줄일 때의 근사·복원 오차<br>**PCA:** 중심화한 feature 행렬의 SVD, 주성분 방향·설명 분산, 저차원 투영·복원<br>**실제 활용:** feature 압축·주요 변화 방향 분석, 선형 최소제곱·기하적 정렬로의 확장, 저랭크 개념과 LoRA의 연결 |
| Embedding Analysis | 분석 방법 | 중요 | **포함 개념:** Feature / Embedding · L2 normalization · Cosine / Euclidean distance · PCA baseline · t-SNE · Perplexity · UMAP · n_neighbors / min_dist · k-NN · Linear probing<br>**표현과 거리:** 분석할 layer·feature 선택, 정규화·거리 정의, 같은 샘플의 학습 전후·모델 간 비교<br>**차원 축소:** PCA를 기준으로 t-SNE·UMAP의 이웃 관계와 저차원 배치 비교, t-SNE의 perplexity·UMAP의 n_neighbors와 min_dist·seed에 따른 시각화 변화<br>**해석과 평가:** 2D 군집 크기·거리·분리의 왜곡 가능성, 원래 feature 공간의 이웃 검색·linear probe로 함께 확인 |
| Least Squares / Robust fitting / RANSAC | 추정 방법 | 중요 | **포함 개념:** Least squares · Residual · Noise / Outlier · Inlier · Minimal sample · Model hypothesis · Consensus · Residual threshold · Max trials / Confidence · Inlier refit<br>**최소제곱:** 관측·모델·파라미터·잔차의 관계, 잔차 제곱합 최소화, 노이즈·이상치에 대한 민감성<br>**RANSAC:** 표본 추출 → 모델 추정 → inlier 판정 → 후보 비교·재추정, 최소 표본 크기·inlier 비율·목표 confidence에 따른 반복 횟수, residual threshold가 inlier 판정·재추정에 미치는 영향<br>**실제 활용:** 이상치가 섞인 직선 피팅으로 시작, feature matching·homography·점군 모델 추정으로 확장, 모델·잔차 정의에 따른 적용 조건 |

### 1. CNN 구조와 활용 모델

#### 학습 목표

Convolution·pooling에서 출발해 residual learning, encoder–decoder와 다중 해상도 feature 구성을 이해하고, 이를 객체 검출·분할의 출력과 학습 구조로 연결한다.

#### 학습 내용

아래 다섯 항목은 개념에 따른 학습 묶음입니다. 각 항목의 분량과 이해의 깊이에 따라 회차를 나눌 수 있습니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Convolution / Pooling | 기초 연산 | 필수 | **포함 개념:** Locality / Weight sharing · Kernel / Stride / Padding / Dilation · Output shape · Receptive field · 1×1 / Group / Depthwise convolution · Parameter count / Computation cost · Max / Average / Global average pooling<br>**필요성:** 이미지의 공간 구조를 활용하는 지역 연결·가중치 공유, 완전 연결 연산과의 차이<br>**공간 연산:** kernel·stride·padding·dilation에 따른 출력 shape·receptive field 계산<br>**연산 비용:** 일반·1×1·group·depthwise convolution의 채널 연결, 파라미터 수·연산량 비교<br>**Pooling:** max·average·global average pooling의 출력, 해상도·정보 손실과 분류 head의 연결 |
| ResNet / Residual Learning | 모델 · Backbone | 필수 | **포함 개념:** Degradation · Residual learning · Identity / Projection shortcut · Basic block / Bottleneck · Stage · Gradient flow · Pre-activation<br>**필요성:** 깊어진 plain network에서 학습 오차까지 커지는 degradation 문제, residual learning의 접근<br>**잔차와 shortcut:** F(x) + x의 의미, residual branch가 학습하는 함수와 identity 경로의 역할<br>**블록과 stage:** basic block·bottleneck, 해상도·채널 변화, identity·projection shortcut의 조건과 gradient 흐름<br>**설계 근거:** shortcut ablation, 원 ResNet과 후속 pre-activation 변형의 차이 |
| Encoder–Decoder / Multi-scale Features | 모델 · 구성 요소 | 필수 | **포함 개념:** Semantic / Instance / Panoptic segmentation · U-Net · Encoder–Decoder · Skip connection / Concatenation · Up-convolution / Crop · FPN · Top-down pathway / Lateral connection · Feature pyramid / Addition<br>**과제 구분:** semantic은 픽셀별 범주, instance는 개별 객체의 mask, panoptic은 모든 픽셀의 범주와 셀 수 있는 객체의 개체 구분을 함께 예측<br>**U-Net · 분할 모델:** 문맥을 얻는 encoder와 위치 정보를 복원하는 decoder, encoder feature의 concatenation과 shape 변화<br>**U-Net 해상도 정렬:** 원 논문의 up-convolution·crop, interpolation 등 후속 구현과의 차이<br>**FPN · Neck:** backbone의 여러 stage → top-down upsampling·lateral 1×1 convolution·addition → 다중 해상도 feature, 결합 전 해상도·채널 정렬<br>**함께 비교:** U-Net의 픽셀별 출력과 FPN의 feature 출력, concatenation·addition의 차이, ResNet shortcut과 각 연결의 목적 비교 |
| Object Detection | 모델 | 필수 | **포함 개념:** Bounding box / Class prediction · Faster R-CNN · RPN / Anchor box / Proposal · RoIPool · Objectness · Box regression · YOLOX · One-stage / Two-stage · Anchor-based / Anchor-free · Multi-scale features · Decoupled head · SimOTA / Dynamic-k assignment · Classification / Objectness / Box loss · IoU / NMS · AP / Latency<br>**문제와 출력:** 여러 객체의 위치·종류 예측, box 좌표 표현·IoU, 분류·objectness·위치 오차의 학습 신호<br>**Faster R-CNN:** 공유 backbone → RPN의 proposal 생성 → RoIPool → 분류·box 보정, anchor·proposal의 정답 할당과 각 loss<br>**YOLOX 구조:** backbone·다중 스케일 neck → 분리된 분류·위치 추정 head, anchor box 없이 grid 위치와 box offset을 이용하는 예측·좌표 변환<br>**YOLOX 학습:** SimOTA의 후보 영역·분류/위치 비용·dynamic-k 양성 예측 선택·중복 할당 해결, 선택 결과에 따른 class·objectness·box loss<br>**학습과 추론:** 정답 할당과 NMS의 역할 구분, YOLOX의 anchor-free 예측에서도 필요한 NMS, Faster R-CNN의 proposal 선택·후처리와 비교<br>**평가와 근거:** AP50·AP@[.5:.95]의 차이, 입력 해상도·장치·batch·정밀도·후처리 포함 여부를 맞춘 latency 비교, YOLOX의 head·anchor-free·정답 할당 ablation |
| Instance Segmentation | 모델 | 중요 | **포함 개념:** Mask R-CNN · Instance mask · RoIPool / RoIAlign · Coordinate quantization · Bilinear sampling · Mask branch / Target · Pixel-wise binary loss · Multi-task learning<br>**필요성:** 객체별 bounding box만으로 표현하기 어려운 경계·형상, semantic segmentation과의 출력 차이<br>**Mask R-CNN 구조:** Faster R-CNN의 분류·box 예측과 병렬로 추가한 mask branch, 검출에서 분할로의 확장<br>**공간 정렬:** RoIPool의 좌표 양자화 문제, RoIAlign의 bilinear sampling과 위치 정보 보존<br>**Mask 학습·추론:** RoI별 mask target·픽셀별 binary loss, 분류·box loss와의 결합, 추론 시 예측 class에 해당하는 mask 선택<br>**설계 근거:** 원 논문의 RoIAlign·mask branch 관련 ablation과 효과가 확인된 조건 |

### 2. Transformer 구조와 비전·멀티모달 활용

#### 학습 목표

Attention·Transformer 블록·위치 표현과 비전 backbone의 동작을 이해하고, 계산·생성 효율화와 검출·dense prediction·prompt 기반 분할·이미지–언어 결합의 구조로 연결한다.

#### 학습 내용

#### 2-A. Attention·Transformer 원리와 비전 백본

아래 다섯 항목으로 공통 원리와 비전 backbone을 공부합니다. 각 항목은 학습 묶음이며, 분량과 이해의 깊이에 따라 회차를 나눌 수 있습니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Attention | 기초 연산 | 필수 | **포함 개념:** Query / Key / Value · Scaled dot-product attention · Softmax axis · Self-attention / Cross-attention · Multi-head attention · Causal / Padding mask · Tensor shape / Computation cost · Permutation equivariance / Position information<br>**필요성:** 토큰마다 필요한 문맥을 다른 토큰에서 가져오는 방식, 입력에 따라 달라지는 정보 결합<br>**계산 흐름:** Q·K·V의 생성과 shape → QKᵀ·√d_k 스케일링 → mask·softmax → V의 가중합, 작은 입력 예제의 값·차원 추적<br>**정보의 출처:** self-attention과 cross-attention에서 Q·K·V를 가져오는 입력, query·key 길이가 다를 때의 출력 shape<br>**Head와 mask:** head별 projection·결합, softmax 정규화 축, causal·padding mask가 허용하는 정보 범위<br>**계산 비용:** 토큰 수에 따른 attention 행렬의 크기·연산량·메모리 사용 변화<br>**위치 정보로 연결:** 위치 정보와 순서 의존 mask가 없을 때 self-attention의 permutation equivariance, 토큰의 내용과 함께 순서·공간 배치를 전달해야 하는 이유 |
| Transformer Architecture | 모델 구조 | 필수 | **포함 개념:** Token embedding · Sinusoidal positional encoding · Encoder / Decoder · FFN · Residual connection · LayerNorm / RMSNorm · Pre-Norm / Post-Norm · GPT / BERT · Next-token prediction · Masked language modeling · Training / Generation<br>**입력과 기본 위치 표현:** token embedding에 sinusoidal positional encoding을 더하는 원 Transformer의 입력, 두 벡터의 차원·역할과 encoder·decoder에 들어가는 위치. 고정된 위치 표현과 학습하는 위치 embedding의 차이<br>**전체 구조:** 위치 정보가 포함된 입력 → encoder의 self-attention·FFN → decoder의 causal self-attention·cross-attention·FFN → 출력, residual·normalization의 연결<br>**블록 변형:** Pre-Norm·Post-Norm의 연산 순서와 gradient 경로, 0장에서 배운 LayerNorm·RMSNorm의 역할을 연결해 비교<br>**GPT 비교 사례:** decoder-only 구조와 causal self-attention, 한 칸 이동한 입력·target의 next-token prediction과 loss<br>**BERT 비교 사례:** encoder-only 구조와 양방향 self-attention, token·segment·position embedding, 가린 token을 맞히는 MLM 입력·target·loss 위치<br>**학습과 활용:** GPT의 학습 시 병렬 계산·자기회귀 생성, BERT의 입력 문맥과 downstream head. GPT·BERT는 구조·정보 범위·학습 목표 비교에 집중하고 세대별 전체 재현은 심화로 확장 |
| Positional Encoding Variants | 구성 요소 | 중요 | **포함 개념:** Learned absolute position · Relative position bias · RoPE · Embedding / Attention score / Q–K injection · 1D / 2D position · Sequence length / Resolution change<br>**비교 출발점:** 02에서 배운 sinusoidal encoding을 기준으로, 위치 정보를 입력 embedding·attention score·Q/K 중 어디에 반영하는지 비교<br>**Learned absolute position:** 위치별 embedding의 학습, 고정된 sinusoidal encoding과의 차이, 학습 범위를 벗어난 길이·해상도의 처리<br>**Relative position bias:** 토큰 간 상대적 거리·방향을 attention score에 반영하는 방식, 상대 위치와 절대 위치의 구분<br>**RoPE:** Q·K에 적용하는 위치별 회전, 두 토큰의 상대 위치가 내적에 반영되는 방식과 적용 지점<br>**비전으로 확장:** 1D 문장 위치와 2D 이미지 위치, ViT·Swin에서의 선택과 해상도·window 크기 변화에 따른 처리 |
| ViT / Swin Transformer | 모델 · Backbone | 필수 | **포함 개념:** ViT · Patch embedding · CLS token / Readout · Learned positional embedding · Global attention · Swin Transformer · Window / Shifted-window attention · Patch merging · Relative position bias · Multi-scale features<br>**ViT:** 이미지 → patch·Linear projection → CLS·위치 embedding → encoder → 분류 출력, 단계별 token 수·shape 추적<br>**ViT 출력·해상도:** 원 모델의 CLS 기반 분류, 해상도 변경 시 위치 embedding 보간, pooling 등 readout 변형과의 차이<br>**Swin:** window 내부 attention과 shifted window의 정보 교환, patch merging에 따른 해상도·채널 변화와 상대 위치 bias<br>**비전 backbone 비교:** ViT의 전역 attention·일정한 token 해상도, Swin·CNN의 계층적 feature, dense prediction에 전달하는 출력<br>**설계 근거:** 국소성·계층 구조 등 inductive bias, 데이터 규모·사전학습·입력 해상도에 따른 성능·계산 비용의 변화 |
| Efficient Attention / KV Cache | 구현 기법 | 중요 | **포함 개념:** Attention computation / Memory cost · FlashAttention · Tiling / Online softmax · GPU memory IO · KV cache · Autoregressive generation · Prefill / Decode · Memory–Computation trade-off<br>**비용의 출처:** projection·attention score·가중합의 연산, 토큰 수에 따른 N×N 행렬과 중간 결과 저장 비용<br>**FlashAttention:** tiling·online softmax로 attention의 수학적 계산을 유지하며 GPU 메모리 이동·중간 행렬 저장을 줄이는 원리. Dense attention의 연산량은 토큰 수에 대해 여전히 이차적으로 증가<br>**KV cache:** 자기회귀 생성에서 이전 토큰의 K·V를 저장·재사용하는 조건, prefill과 토큰별 decode, 층별 cache의 shape·메모리 증가<br>**적용 범위 비교:** FlashAttention의 학습·추론 계산과 KV cache의 생성 시 재사용, 계산 절감·메모리 사용의 교환 관계<br>**학습 깊이:** 작은 예제로 cache 유무의 계산 흐름·메모리 사용 비교, GPU kernel 구현과 세부 최적화는 선택 심화 |

#### 2-B. 비전 과제와 멀티모달 활용

1장의 검출·분할과 연결해 출력 구조를 비교합니다. VLM에서는 이미지·언어의 연결 구조를 먼저 이해하고, CLIP 등 표현 학습의 원리는 3장에서 이어서 공부합니다.

| 학습 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DETR / End-to-End Detection | 모델 | 필수 | **포함 개념:** DETR · Set prediction · Object query · CNN backbone / Transformer encoder–decoder · Bipartite / Hungarian matching · Matching cost / Training loss · No-object class · Bounding box prediction · NMS-free inference · YOLOv10 · One-to-many / One-to-one heads · Consistent matching metric · Top-one assignment<br>**필요성:** 객체의 순서가 정해지지 않은 정답 집합, 예측 중복과 정답 할당을 함께 다루는 set prediction<br>**DETR 구조:** CNN feature·위치 정보 → encoder → learned object query를 사용하는 decoder → 고정 개수의 class·box 예측<br>**DETR 학습:** Hungarian matching의 비용과 matching 후 계산하는 class·box loss의 차이, unmatched query의 no-object 처리<br>**YOLOv10 비교:** 학습 시 one-to-many·one-to-one head를 함께 사용하고, 추론 시 one-to-one head로 예측하는 흐름. 풍부한 학습 신호와 중복 예측 억제의 역할 분담<br>**할당 방식 비교:** YOLOv10의 class score·IoU 기반 일관된 matching metric과 top-one 선택, DETR의 Hungarian matching과 다른 계산 방식<br>**1장과 연결:** Faster R-CNN·YOLOX의 proposal·밀집 예측·정답 할당·NMS와 비교, anchor-free 여부와 NMS-free 여부를 구분. YOLOv10의 비교 범위는 두 head·할당·loss·추론 경로 |
| Dense Prediction / DPT | 모델 | 필수 | **포함 개념:** Dense prediction · Depth / Semantic segmentation · ViT / Hybrid backbone · Intermediate tokens · Reassemble · Spatial feature map · Multi-resolution fusion · Convolutional decoder<br>**필요성:** 이미지 단위 표현에서 픽셀별 깊이·범주 출력으로의 전환, 문맥과 공간 위치를 함께 보존하는 decoder의 역할<br>**DPT 동작:** backbone의 여러 층에서 얻은 token → 공간 feature 재배열·해상도 변환 → convolutional decoder의 점진적 fusion → 픽셀별 출력<br>**학습과 출력:** 깊이 추정·semantic segmentation의 target·출력 채널·loss 차이, backbone과 task별 head의 연결<br>**1장·backbone과 비교:** vanilla ViT의 중간 층이 처음부터 해상도 pyramid인 것은 아니라는 점, Swin·FPN·U-Net의 feature·복원 경로와 차이 |
| Promptable Segmentation / SAM | 모델 | 중요 | **포함 개념:** SAM · Image encoder · Prompt encoder · Point / Box / Mask prompt · Mask decoder · Cross-attention · Multiple masks / Quality prediction · Image embedding reuse · SAM 2 / Streaming memory<br>**필요성:** 점·박스·mask 지시에 따라 달라지는 분할 대상, 고정된 범주 예측과 prompt 기반 분할의 차이<br>**원 SAM 구조:** image encoder·prompt encoder·mask decoder, 이미지·prompt 표현의 정보 교환과 mask 생성<br>**학습·추론:** 데이터·prompt sampling·mask loss, 모호한 prompt에 대한 복수 mask·품질 예측, 같은 이미지에 대한 embedding 재사용<br>**SAM 2 비교:** streaming memory와 프레임별 prompt·mask 처리, 이미지 분할에서 비디오 처리로 확장하며 추가된 정보 흐름<br>**학습 범위:** 원 SAM의 구조·학습·추론을 중심으로 후속 변화를 비교하고, 버전별 전체 구조·평가는 선택 심화 |
| VLM / Visual Tokens | 모델 | 중요 | **포함 개념:** LLaVA · Vision encoder · Projector · LLM · Visual tokens · Image–Text token sequence · Feature alignment / Instruction tuning · Frozen / Trainable parameters · Next-token loss · Autoregressive response generation<br>**필요성:** 이미지 표현과 언어 모델의 token 표현 연결, 시각 정보가 질문의 문맥과 응답에 반영되는 경로<br>**원 LLaVA 구조:** 사전학습 vision encoder → linear projector → visual token, 텍스트 token과 함께 LLM에 입력되는 위치·shape와 응답 생성<br>**두 단계 학습:** feature alignment에서 projector 학습, instruction tuning에서 projector·LLM 학습. 두 단계 모두 vision encoder 고정, 단계별 데이터·target·gradient 경로 비교<br>**학습과 생성:** 정답 응답 위치의 next-token loss, 학습 시 제공되는 응답과 생성 시 이전 token을 이용하는 흐름의 차이<br>**3장과 연결:** CLIP의 이미지–텍스트 표현 정렬과 VLM의 응답 생성 목적 구분, 사전학습·전이·fine-tuning의 원리와 근거 |

### 3. 표현 학습과 모델 적응

#### 학습 목표

표현을 얻는 학습 목표와 teacher·target의 역할을 이해하고, pretraining 모델을 활용·적응하는 방법을 구분한다.

#### 학습 내용

| 개념 / 모델 / 기법 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Pretraining / Transfer Learning | 학습 방법 | 필수 | **학습 단계:** pretraining과 downstream task에서 데이터·target·head가 어떻게 달라지는지 구분한다.<br>**적응 범위:** frozen feature·linear probing·부분 및 전체 fine-tuning에서 고정·갱신하는 파라미터를 비교한다.<br>**실험 해석:** 사전학습 데이터와 학습 조건을 확인하고, 증강·regularization·평가 시 데이터 누수를 기초 원리와 연결한다. |
| SimCLR | 학습 방법 | 필수 | **학습 쌍:** 같은 이미지의 두 augmentation을 positive로, batch의 다른 이미지에서 얻은 view를 negative로 사용하는 구성을 이해한다.<br>**목표와 구조:** NT-Xent·temperature, encoder representation과 projection head 출력의 차이를 추적한다.<br>**비교와 주의:** 증강·batch 크기의 영향을 확인한다. 여기서 view는 증강한 이미지이며, 다른 카메라에서 촬영한 multi-view와 구분한다. |
| CLIP | 모델 | 필수 | **이미지–텍스트 정렬:** 두 encoder가 paired image·text를 공통 embedding 공간으로 보내는 흐름을 이해한다.<br>**학습 목표:** batch 내 정답 pair와 나머지 pair, 정규화된 embedding·temperature·양방향 contrastive loss를 연결한다.<br>**Zero-shot 추론:** class 이름을 prompt 문장으로 바꿔 text embedding을 만들고, image embedding과의 유사도로 분류하는 과정을 추적한다. |
| SigLIP | 모델 · 학습 방법 | 중요 | **Pairwise 목표:** image–text pair의 일치 여부를 sigmoid loss로 학습하는 방식을 이해한다.<br>**CLIP과 비교:** batch 전체 유사도의 softmax 정규화와 pairwise sigmoid의 차이, positive·negative pair 구성과 bias·scale을 확인한다.<br>**설계 근거:** batch 크기·pair 비율·학습 조건을 확인하며 원 논문의 ablation을 읽는다. |
| Knowledge distillation | 학습 방법 | 필수 | **Teacher와 student:** teacher의 soft target으로 student를 학습시키는 목적과 temperature의 역할을 이해한다.<br>**Loss와 gradient:** soft-target loss·hard-label loss의 결합, teacher 고정과 student 업데이트를 수식·코드로 추적한다.<br>**후속 비교:** 원 논문의 목표·실험을 기준으로 feature distillation, DINO의 self-distillation·EMA teacher와 차이를 연결한다. |
| DINO | 학습 방법 | 필수 | **원 DINO:** 같은 이미지의 서로 다른 crop에서 teacher·student의 출력 분포를 맞추는 self-distillation을 이해한다.<br>**학습 안정화:** multi-crop, EMA teacher·stop-gradient, centering·sharpening과 collapse 방지의 관계를 추적한다.<br>**후속 비교:** DINOv2의 image·patch-level 목표와 데이터·학습 레시피, DINOv3의 Gram anchoring을 비교한다. 버전별 전체 구조·목표는 별도 심화로 다룬다. |
| MAE | 학습 방법 | 필수 | **Masked reconstruction:** 일부 patch를 가리고, 보이는 patch만 encoder에 넣어 가린 영역의 픽셀을 복원하는 목표를 이해한다.<br>**비대칭 구조:** encoder 출력을 원래 위치에 놓고 mask token을 더해 작은 decoder로 보내는 과정과, masked 영역의 pixel 복원 loss를 추적한다.<br>**학습과 전이:** pretraining의 decoder와 downstream head를 구분하고, masking 비율·연산량·표현 학습의 관계를 살펴본다. |
| SimMIM | 학습 방법 | 중요 | **단순한 복원 목표:** 가린 위치를 mask token으로 대체한 입력에서 원래 RGB 값을 회귀하는 학습을 이해한다.<br>**구조와 loss:** encoder 뒤의 가벼운 prediction head, masked 영역의 L1 loss와 patch·mask 크기를 확인한다.<br>**MAE와 비교:** mask token의 encoder 통과 여부, decoder·head의 크기, pixel 복원 목표의 차이를 비교한다. |
| BEiT | 학습 방법 | 중요 | **Discrete target:** 별도로 사전학습한 visual tokenizer가 만든 discrete token을 가린 위치의 정답으로 사용하는 원 BEiT를 이해한다.<br>**학습 흐름:** mask token을 포함한 입력, Transformer·prediction head, token 분류 loss와 tokenizer의 역할을 구분한다.<br>**비교:** MAE·SimMIM의 pixel 회귀와 target·head의 차이를 비교한다. 후속 BEiT 버전의 전체 재현은 선택 심화로 둔다. |
| LoRA | 적응 방법 | 중요 | **Low-rank update:** 사전학습 가중치는 고정하고, 가중치 변화량을 두 작은 행렬의 곱으로 학습하는 원리를 이해한다.<br>**파라미터와 gradient:** 적용 위치·rank·scale, 두 행렬의 초기화와 gradient 흐름을 전체 fine-tuning과 비교한다.<br>**학습과 배포:** 가중치에 update를 합치는 조건과 비용을 확인하고, 원 논문의 ablation 및 PEFT 안에서의 역할을 살펴본다. |

---

### 4. 생성 모델

#### 학습 목표

생성 목표, latent 표현, 네트워크 구조와 sampling 과정을 연결해 이해한다.

#### 학습 내용

#### 4.1 VAE · GAN · Autoregressive · VQ

| 모델 / 방법 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| VAE | 생성 모델 | 필수 | **잠재변수 모델:** encoder가 근사 posterior를, decoder가 관측 데이터의 분포를 나타내는 구조를 이해한다.<br>**학습 목표:** ELBO의 reconstruction·KL 항, prior와 posterior, reparameterization을 통한 gradient 흐름을 연결한다.<br>**복원과 생성:** 입력을 encoding한 뒤 복원하는 과정과, prior에서 latent를 뽑아 새 샘플을 만드는 과정을 구분한다. |
| GAN | 생성 모델 | 중요 | **적대적 학습:** noise를 데이터로 바꾸는 generator와, 실제·생성 데이터를 구분하는 discriminator의 역할을 이해한다.<br>**두 모델의 갱신:** 원 minimax 목표와 generator의 non-saturating 목표를 구분하고, 번갈아 학습할 때의 gradient 흐름을 추적한다.<br>**학습과 추론:** 불안정성·mode collapse의 의미를 살펴보고, 생성 시에는 generator를 사용하는 흐름을 확인한다. |
| Autoregressive Models | 생성 모델 | 중요 | **순차 확률 분해:** 앞선 픽셀·토큰을 조건으로 다음 값을 예측하며 이미지의 확률을 구성하는 원리를 이해한다.<br>**대표 모델:** PixelCNN의 masked convolution·학습 target을 확인하고, 정답 문맥을 쓰는 학습과 생성 문맥을 쓰는 순차 sampling을 비교한다.<br>**확장과 비용:** 순차 추론의 비용을 확인하고, pixel 공간에서 latent token 공간으로 옮기는 연결을 VQ-VAE·VQGAN에서 살펴본다. |
| VQ-VAE | 생성 모델 | 중요 | **이산 latent:** encoder 출력을 codebook의 가까운 벡터로 치환해 decoder에 전달하는 vector quantization을 이해한다.<br>**학습과 gradient:** reconstruction·codebook·commitment loss, stop-gradient와 straight-through 추정의 역할을 추적한다.<br>**생성의 두 단계:** autoencoder 학습과 code index의 prior 학습을 구분한다. 생성 시 prior → codebook → decoder의 흐름을 연속 latent VAE와 비교한다. |
| VQGAN | 생성 모델 | 중요 | **Tokenizer 학습:** encoder·codebook·decoder와 discriminator를 확인하고, reconstruction·perceptual·adversarial 목표의 역할을 구분한다.<br>**Prior 학습:** tokenizer를 학습한 뒤, 이미지 code의 배열을 예측하는 autoregressive Transformer를 별도로 학습하는 두 단계를 추적한다.<br>**생성과 비교:** token sampling → codebook → decoder의 흐름을 확인하고, VQ-VAE와 구조·목표·이미지 표현을 비교한다. |

#### 4.2 Diffusion · Flow Matching

| 모델 / 방법 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DDPM | 생성 모델 | 필수 | **Noising과 denoising:** forward에서 noise를 더하는 과정과, 학습한 역방향 전이로 noise에서 이미지를 생성하는 과정을 구분한다.<br>**학습 목표:** 임의의 timestep에서 noisy 입력을 만들고 ε를 예측하는 목표, noise schedule과 시간 조건을 수식·코드로 연결한다.<br>**Sampling:** ε 예측으로 역방향 평균을 계산하고 noise를 주입하는 반복 절차를 추적한다. 학습에 쓰는 정답 이미지와 생성 시 입력을 구분한다. |
| DDIM | 생성 방법 | 필수 | **학습과 sampling 분리:** DDPM의 ε-prediction 목표로 학습한 denoiser를 활용하면서 sampling 갱신식을 바꾸는 방법을 이해한다.<br>**갱신식과 경로:** 현재 noisy sample → 원본 추정 → 다음 sample의 계산과, η가 추가 noise를 조절하는 역할을 추적한다.<br>**속도와 결과:** 같은 초기 noise에서 η=0일 때의 결정적 sampling을 확인하고, timestep 부분집합·sampling 단계 수에 따른 비용과 품질을 비교한다. |
| Score-based Generative Models | 생성 모델 | 필수 | **Score의 의미:** noise가 섞인 데이터 분포의 log-density를 입력으로 미분한 gradient를 학습한다는 관점을 이해한다.<br>**원 방법:** noise-conditioned score network와 denoising score matching, 여러 noise 수준을 거치는 annealed Langevin sampling을 추적한다.<br>**Diffusion과 연결:** Gaussian perturbation에서 score와 ε-prediction의 관계를 확인한다. SDE·probability flow ODE 정식화는 후속 심화로 구분한다. |
| Latent Diffusion | 생성 모델 | 필수 | **학습 단계:** 먼저 학습한 autoencoder로 이미지를 압축한 뒤, latent 공간에서 denoiser를 학습하는 두 단계를 구분한다.<br>**조건과 생성:** condition·cross-attention·classifier-free guidance의 역할과 noise latent → denoising → 이미지 decoder의 흐름을 추적한다.<br>**Autoencoder 비교:** KL·VQ regularization 및 perceptual·adversarial reconstruction을 VAE·VQGAN과 연결한다. Stable Diffusion은 후속 활용으로 살펴본다. |
| ControlNet | 모델 · 조건 제어 | 중요 | **공간 조건:** edge·depth·pose 등의 조건을 사전학습 text-to-image diffusion 모델에 추가하는 구조를 이해한다.<br>**학습 구조:** 고정된 backbone, trainable branch와 zero-initialized convolution이 연결되는 위치와 gradient 흐름을 추적한다.<br>**설계 이유:** 초기에는 원 모델의 출력을 유지하며 조건 제어를 학습하는 원리와, 추론 시 조건의 영향을 확인한다. |
| DiT | 모델 · Denoiser | 필수 | **Transformer denoiser:** 원 DiT에서 autoencoder latent를 patch token으로 바꿔 Transformer로 처리하는 흐름을 이해한다.<br>**조건 주입:** timestep·class embedding, adaLN-Zero와 출력 head를 추적하고, ε와 역방향 분산을 예측하는 원 모델을 확인한다.<br>**구조 비교:** U-Net denoiser와 비교하고, latent patch 크기·모델 규모·계산량을 바꾼 ablation으로 설계를 검토한다. |
| Flow Matching | 생성 방법 | 필수 | **Probability path:** noise 분포와 data 분포를 잇는 경로를 정하고, 그 분포의 변화를 만드는 시간 의존 velocity field를 학습하는 관점을 이해한다.<br>**학습과 생성:** conditional path에서 만든 velocity target의 회귀와, 학습한 field를 ODE로 적분하는 sampling을 구분한다.<br>**비교와 연결:** 경로 선택과 학습 target을 DDPM의 noise 예측과 비교하고, 다음 Rectified Flow의 직선 보간 목표에 연결한다. |
| Rectified Flow | 생성 방법 | 필수 | **직선 보간 학습:** noise–data pair를 잇는 직선 위에서 두 끝점의 차이를 velocity target으로 회귀하는 방법을 이해한다.<br>**실제 생성 경로:** 학습에 쓴 직선 보간과, 학습한 field를 적분해 얻는 ODE 경로가 항상 같거나 직선인 것은 아님을 구분한다.<br>**Coupling과 reflow:** 생성한 pair로 다시 학습하는 reflow, 경로의 직선성·sampling 단계 수의 관계를 확인하고 Flow Matching과 비교한다. |
| Video Diffusion | 생성 모델 | 중요 | **시간 축 확장:** 대표 논문 한 편을 정해 video tensor·조건 입력·학습 target과 생성 과정을 추적한다.<br>**공간·시간 처리:** spatial·temporal 연산 또는 attention이 프레임 내부와 프레임 사이 정보를 결합하는 방식을 이해한다.<br>**평가와 범위:** 이미지 품질과 시간적 일관성을 구분해 평가한다. 다른 영상 모델의 구조·조건 방식은 후속 비교로 다룬다. |

