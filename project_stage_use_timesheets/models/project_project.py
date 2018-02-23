# -*- coding: utf-8 -*-
# © 2015-17 Eficent Business and IT Consulting Services S.L.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import api, models


class ProjectProject(models.Model):
    _inherit = 'project.project'

    @api.multi
    def write(self, values):
        for project in self:
            stage = project.analytic_account_id.stage_id
            if stage.allow_timesheets and project.account_class == \
                    'work_package':
                values['allow_timesheets'] = True
            else:
                values['allow_timesheets'] = False
        return super(ProjectProject, self).write(values)
