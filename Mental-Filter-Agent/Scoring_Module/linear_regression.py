"""
Mental Filter - Linear Regression Scoring Module
基于 KADS-11 特征的多元线性回归计分与极高危预警节点
设计者：周鹏云
"""

async def main(args):
    # 兼容工作流引擎的传参格式
    params = args.params if hasattr(args, 'params') else args
    
    # 1. 获取上游特征提取模型输出的 JSON 字典
    # 预期格式: {"X1": 1, "X2": 0, ..., "X11": 0}
    features = params.get('extracted_features', {})
    
    # 2. 回归系数 (Beta Weights) 
    # 注：此处系基于模拟生成的预实验数据拟合的占位权重 (R-squared=1.0)
    # 投入真实临床测试后，须替换为基于真实样本跑出的回归系数
    weights = {
        "X1": 1.0, "X2": 1.0, "X3": 1.0, "X4": 1.0, 
        "X5": 1.0, "X6": 1.0, "X7": 1.0, "X8": 1.0, 
        "X9": 1.0, "X10": 1.0, "X11": 1.0
    }
    
    # 截距 (Intercept)
    intercept = 0.0 
    
    # 3. 计算回归总分 Y = Intercept + Σ(βi * Xi)
    total_score = intercept
    for symptom, value in features.items():
        weight = weights.get(symptom, 0)
        total_score += float(value) * weight
        
    # 4. 危机预警阈值判定 (Thresholding & Red-line)
    # 临床高危红线法则：无论总分多少，只要触发 X11（自伤/自杀意念），强制一票否决为高危！
    is_risk = "是" if (features.get("X11", 0) > 0 or total_score >= 8.0) else "否"

    return {
        "regression_score": round(total_score, 2),
        "risk_status": is_risk
    }