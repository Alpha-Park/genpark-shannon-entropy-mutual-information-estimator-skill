"""MCP Server for Information Theory Estimator Skill."""
import json
import sys
from client import InformationTheoryEstimator

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method")
            params = req.get("params", {})

            if method == "tools/list":
                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "tools": [{
                            "name": "estimate_information_metrics",
                            "description": "Calculate Shannon Entropy, KL Divergence, and Mutual Information",
                            "inputSchema": {
                                "type": "object",
                                "properties": {
                                    "probabilities": {"type": "array", "items": {"type": "number"}},
                                    "target_probabilities": {"type": "array", "items": {"type": "number"}},
                                    "joint_matrix": {"type": "array", "items": {"type": "array", "items": {"type": "number"}}}
                                }
                            }
                        }]
                    }
                }
            elif method == "tools/call":
                args = params.get("arguments", {})
                out = {}
                if "probabilities" in args:
                    out["entropy"] = InformationTheoryEstimator.entropy(args["probabilities"])
                if "probabilities" in args and "target_probabilities" in args:
                    out["kl_divergence"] = InformationTheoryEstimator.kl_divergence(args["probabilities"], args["target_probabilities"])
                    out["jensen_shannon"] = InformationTheoryEstimator.jensen_shannon_divergence(args["probabilities"], args["target_probabilities"])
                if "joint_matrix" in args:
                    out["mutual_information"] = InformationTheoryEstimator.mutual_information(args["joint_matrix"])

                res = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {"content": [{"type": "text", "text": json.dumps(out)}]}
                }
            else:
                res = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}
            print(json.dumps(res), flush=True)
        except Exception as e:
            err = {"jsonrpc": "2.0", "id": None, "error": {"code": -32000, "message": str(e)}}
            print(json.dumps(err), flush=True)

if __name__ == "__main__":
    main()
