from lib import actions

class GetResultArtifact(actions.BaseAction):
    def run(self, uuid, report_uuid, artifact_name, raw=False, verify=True):

        client = self.client
        response = client.get_result_artifact(uuid, report_uuid, artifact_name,
                                              raw, verify)

        return response
