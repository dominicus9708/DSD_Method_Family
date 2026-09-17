# BH-RB-025 — finite-relaxation causal transport response gate

## 목적

BH-RB-024에서는 trapped synthetic shell에서 compactness를 비증가시키는 데 필요한 내부 outward flux의 임계값을 구했고, 일부 빠른 붕괴 branch에서 그 flux가 radial NEC 필요조건과 양립할 수 있음을 확인했다.

BH-RB-025에서는 flux를 순간적으로 지정하지 않고 최소 finite-relaxation transport control

\[
\tau_q \frac{dQ}{dt}+Q=Q_{\rm drive}
\]

을 둔다.

이 식은 Maxwell–Cattaneo형 최소 control이며, full Israel–Stewart black-hole interior solution이 아니다.
목적은 오직 다음을 검사하는 것이다.

1. finite relaxation이 새로운 독립 시간척도 조건을 만드는가.
2. BH-RB-024의 \(Q_{\rm crit}\)를 실제로 넘기려면 어떤 drive amplitude와 지속시간이 필요한가.
3. relaxation lag 동안 compactness가 먼저 증가하는 overshoot가 불가피한가.
4. 이 결과만으로 persistent finite 3D core를 주장하지 않는다.

## BH-RB-024에서 유지하는 shell control

기하단위 \(G=c=1\)에서

\[
\mathcal C=\frac{2m}{R},
\qquad
E=8\pi\rho R^2,
\qquad
P=8\pi p_rR^2,
\qquad
Q=8\pi qR^2.
\]

붕괴속도 \(V=-U>0\)에 대해

\[
\Gamma^2=1+V^2-\mathcal C
\]

이고 short-time frozen-shell control에서

\[
R D_T\mathcal C
=
V(\mathcal C+P)-Q\Gamma.
\]

따라서 compactness가 감소하기 시작하려면

\[
\boxed{
Q>Q_{\rm crit}
=
\frac{V(\mathcal C+P)}{\Gamma}
}
\]

가 필요하다.

radial null NEC의 필요한 조건은

\[
\rho+p_r\ge 2|q|
\]

이므로 dimensionless flux에는

\[
\boxed{
|Q|\le Q_{\rm NEC}
=
\frac{E+P}{2}.
}
\]

## finite-relaxation 해

초기값 \(Q(0)=0\), 상수 thermodynamic drive를 사용하면

\[
Q(t)
=
Q_{\rm drive}
\left(1-e^{-t/\tau_q}\right).
\]

따라서

\[
Q_{\rm drive}\le Q_{\rm crit}
\]

이면 아무리 오래 기다려도 threshold를 넘지 못한다.

반대로

\[
Q_{\rm drive}>Q_{\rm crit}
\]

이면 최초 threshold crossing time은

\[
\boxed{
\frac{t_{\rm cross}}{\tau_q}
=
-\ln\left(
1-\frac{Q_{\rm crit}}{Q_{\rm drive}}
\right).
}
\]

즉 amplitude 조건 외에

\[
\boxed{
T_{\rm available}
\gtrsim
t_{\rm cross}
}
\]

라는 독립적인 시간척도 조건이 생긴다.

## relaxation overshoot

frozen background에서 compactness 변화량은

\[
\frac{R\Delta\mathcal C}{\tau_q}
=
\Gamma
\left[
(Q_{\rm crit}-Q_{\rm drive})y
+
Q_{\rm drive}(1-e^{-y})
\right],
\qquad
y=\frac{t}{\tau_q}.
\]

\(t=t_{\rm cross}\)까지는 integrand가 양수이므로 compactness는 먼저 증가한다.

즉

\[
\boxed{
\text{causal finite relaxation}
\Rightarrow
\text{threshold crossing 이전의 compactness overshoot}.
}
\]

threshold를 넘긴 뒤에도 이미 생긴 overshoot를 되돌리려면 더 긴 시간이 필요하다.
return time \(t_{\rm return}\)은

\[
(Q_{\rm crit}-Q_{\rm drive})y
+
Q_{\rm drive}(1-e^{-y})
=0
\]

의 양의 해이다.

## synthetic control

BH-RB-024와 동일하게

\[
\mathcal C=1.2,
\qquad
E=3\mathcal C=3.6
\]

을 homogeneous synthetic comparator로만 사용한다.

BH-RB-020/021 normalized EOS에서는 geometry를 가져오지 않고 오직

\[
w=\frac{p}{\varepsilon}
\simeq 0.065753984128
\]

만 사용하여

\[
P=wE
\simeq0.236714342862
\]

를 둔다.

따라서

\[
Q_{\rm NEC}
\simeq1.918357171431.
\]

### slow branch

\[
V=0.5
\]

이면

\[
Q_{\rm crit}
\simeq3.212590934889
>
Q_{\rm NEC}.
\]

따라서 NEC-compatible drive는 finite relaxation 여부와 무관하게 threshold에 도달할 수 없다.

\[
\boxed{
Q_{\rm drive}\le Q_{\rm NEC}<Q_{\rm crit}.
}
\]

### fast branch

\[
V=0.8
\]

이면

\[
\Gamma
\simeq0.663324958071,
\]

\[
Q_{\rm crit}
\simeq1.732742693162
<
Q_{\rm NEC}.
\]

control drive를

\[
Q_{\rm drive}
=
0.95Q_{\rm NEC}
\simeq1.822439312860
\]

으로 두면

\[
\boxed{
\frac{t_{\rm cross}}{\tau_q}
\simeq3.011498080667
}
\]

이고 compactness overshoot는 frozen normalization에서

\[
\frac{R\Delta\mathcal C_{\rm cross}}{\tau_q}
\simeq0.970193341912>0.
\]

overshoot를 원래 compactness까지 되돌리는 시간은

\[
\boxed{
\frac{t_{\rm return}}{\tau_q}
\simeq20.317814832694.
}
\]

NEC 한계를 완전히 포화하는 가장 빠른 허용 drive를 써도

\[
\frac{t_{\rm cross,best}}{\tau_q}
\simeq2.335552633650,
\]

\[
\frac{t_{\rm return,best}}{\tau_q}
\simeq10.334834210417.
\]

즉 NEC-compatible amplitude window가 있다는 사실만으로는 충분하지 않다.

\[
\boxed{
\text{필요한 flux amplitude}
+
\text{충분히 작은 }\tau_q
+
\text{충분한 지속시간}
}
\]

이 동시에 필요하다.

## 물리적 의미

이번 단계에서 살아남은 조건은

\[
\boxed{
Q_{\rm drive}>Q_{\rm crit}
}
\]

과

\[
\boxed{
\frac{T_{\rm available}}{\tau_q}
\ge
-\ln\left(
1-\frac{Q_{\rm crit}}{Q_{\rm drive}}
\right).
}
\]

그러나 \(Q_{\rm drive}\) 자체는 아직 도출되지 않았다.
실제 물리에서는 temperature gradient, chemical-potential gradient, acceleration coupling, conductivity, relaxation coefficients 등이 constitutive transport closure에서 공급되어야 한다.

상대론적 dissipative-collapse 문헌에서 Misner–Sharp dynamics를 causal Israel–Stewart transport와 결합하는 경로가 존재하지만, 이번 감사는 그 full equation을 black-hole core에 적용한 것이 아니다.

## 방화벽

- Maxwell–Cattaneo control은 full Israel–Stewart transport가 아니다.
- \(Q_{\rm drive}\)는 DSD나 EOS label만으로 자동 생성되지 않는다.
- internal outward flux는 event horizon 밖으로의 energy escape를 뜻하지 않는다.
- short-time frozen-shell control은 global detrapping을 증명하지 않는다.
- \(Q>Q_{\rm crit}\)가 잠시 성립해도 persistent 3D core support는 도출되지 않는다.
- 실제 다음 단계에서는 transport coefficients와 thermodynamic gradients의 provenance가 필요하다.

## 계산 감사

Python 감사 결과:

\[
\boxed{23/23\ {\rm PASS}}
\]

판정:

`PASS_WITH_BOUNDARY / FINITE_RELAXATION_ADDS_A_TRANSPORT_TIMESCALE_GATE / NEC_COMPATIBLE_DRIVE_CAN_CROSS_QCRIT_ONLY_IN_THE_FAST_SYNTHETIC_BRANCH / RELAXATION_LAG_CAUSES_INITIAL_COMPACTNESS_OVERSHOOT / AMPLITUDE_AND_AVAILABLE_DURATION_REQUIRE_EXPLICIT_CONSTITUTIVE_THERMODYNAMIC_CLOSURE / FULL_ISRAEL_STEWART_GR_EVOLUTION_AND_PERSISTENT_3D_CORE_NOT_DERIVED`

## 다음 본선 — BH-RB-026

다음에는 \(Q_{\rm drive}\)를 상수로 임의 입력하지 않고, thermodynamic gradients와 explicit transport coefficients에서 생성되는 최소 constitutive driver를 둔다.

최소 목표는

\[
Q_{\rm drive}
=
\mathcal D[
\nabla T,
\nabla\mu,
a^\mu,
\kappa,
\tau_q,\ldots
]
\]

형태의 provenance를 만들고,

\[
Q_{\rm drive}>Q_{\rm crit}
\]

가 가능한 parameter region이 존재하는지 검사하는 것이다.

그 뒤에야 compactness evolution과 support-volume evolution을 동시에 적분하는 단계로 넘어간다.
