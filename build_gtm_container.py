import json

def generate_gtm_json(gtm_id="GTM-P2Z4TZ4Z", ga4_id="G-NQC5PHY67R"):
    num_acc = "10000001"
    num_cnt = "20000001"
    
    container = {
        "exportFormatVersion": 2,
        "exportTime": "2026-09-09 22:00:00",
        "containerVersion": {
            "path": f"accounts/{num_acc}/containers/{num_cnt}/versions/0",
            "accountId": num_acc,
            "containerId": num_cnt,
            "containerVersionId": "0",
            "name": "CV Ejecutivo Inteligente",
            "publicId": gtm_id,
            "container": {
                "path": f"accounts/{num_acc}/containers/{num_cnt}",
                "accountId": num_acc,
                "containerId": num_cnt,
                "name": "CV Ejecutivo Inteligente",
                "publicId": gtm_id,
                "usageContext": ["WEB"]
            },
            "tag": [
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "1",
                    "name": "Google Tag - GA4 Configuration (CV Ejecutivo Inteligente)",
                    "type": "googtag",
                    "parameter": [
                        {"type": "BOOLEAN", "key": "tagIdSettings", "value": "false"},
                        {"type": "TEMPLATE", "key": "tagId", "value": ga4_id}
                    ],
                    "firingTriggerId": ["2147479553"]  # All Pages
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "2",
                    "name": "GA4 Event - cv_kpi_interaction",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_kpi_interaction"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "kpi_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - kpi_id}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "kpi_number"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - kpi_number}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "kpi_label"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - kpi_label}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "target_anchor"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - target_anchor}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - candidate_id}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["101"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "3",
                    "name": "GA4 Event - cv_cert_filter",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_cert_filter"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "filter_category"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - filter_category}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - candidate_id}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["102"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "4",
                    "name": "GA4 Event - cv_document_download",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_document_download"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "document_type"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - document_type}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "document_name"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - document_name}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["103"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "5",
                    "name": "GA4 Event - cv_scroll_depth",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_scroll_depth"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "depth_percentage"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - depth_percentage}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["104"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "6",
                    "name": "GA4 Event - cv_theme_toggle",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_theme_toggle"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "theme_applied"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - theme_applied}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["105"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "7",
                    "name": "GA4 Event - cv_language_switch",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_language_switch"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "selected_language"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - selected_language}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["106"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "8",
                    "name": "GA4 Event - cv_external_click",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "cv_external_click"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "link_type"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - link_type}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "target_url"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - target_url}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["107"]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "tagId": "9",
                    "name": "GA4 Event - telegram_alert_dispatch",
                    "type": "gaawe",
                    "parameter": [
                        {"type": "TEMPLATE", "key": "measurementIdOverride", "value": ga4_id},
                        {"type": "TEMPLATE", "key": "eventName", "value": "telegram_alert_dispatch"},
                        {
                            "type": "LIST",
                            "key": "eventParameters",
                            "list": [
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "alert_type"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - alert_type}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "lead_action"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - lead_action}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "user_location"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - user_location}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "device_type"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - device_type}}"}
                                    ]
                                },
                                {
                                    "type": "MAP",
                                    "map": [
                                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"},
                                        {"type": "TEMPLATE", "key": "value", "value": "{{dlv - candidate_id}}"}
                                    ]
                                }
                            ]
                        }
                    ],
                    "firingTriggerId": ["108"]
                }
            ],
            "trigger": [
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "101",
                    "name": "Custom Event - cv_kpi_interaction",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_kpi_interaction"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "102",
                    "name": "Custom Event - cv_cert_filter",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_cert_filter"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "103",
                    "name": "Custom Event - cv_document_download",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_document_download"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "104",
                    "name": "Custom Event - cv_scroll_depth",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_scroll_depth"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "105",
                    "name": "Custom Event - cv_theme_toggle",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_theme_toggle"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "106",
                    "name": "Custom Event - cv_language_switch",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_language_switch"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "107",
                    "name": "Custom Event - cv_external_click",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "cv_external_click"}
                            ]
                        }
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "triggerId": "108",
                    "name": "Custom Event - telegram_alert_dispatch",
                    "type": "CUSTOM_EVENT",
                    "customEventFilter": [
                        {
                            "type": "EQUALS",
                            "parameter": [
                                {"type": "TEMPLATE", "key": "arg0", "value": "{{_event}}"},
                                {"type": "TEMPLATE", "key": "arg1", "value": "telegram_alert_dispatch"}
                            ]
                        }
                    ]
                }
            ],
            "variable": [
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "201",
                    "name": "dlv - kpi_id",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "kpi_id"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "202",
                    "name": "dlv - kpi_number",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "kpi_number"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "203",
                    "name": "dlv - kpi_label",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "kpi_label"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "204",
                    "name": "dlv - target_anchor",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "target_anchor"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "205",
                    "name": "dlv - filter_category",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "filter_category"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "206",
                    "name": "dlv - document_type",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "document_type"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "207",
                    "name": "dlv - document_name",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "document_name"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "208",
                    "name": "dlv - depth_percentage",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "depth_percentage"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "209",
                    "name": "dlv - theme_applied",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "theme_applied"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "210",
                    "name": "dlv - selected_language",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "selected_language"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "211",
                    "name": "dlv - link_type",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "link_type"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "212",
                    "name": "dlv - target_url",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "target_url"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "213",
                    "name": "dlv - candidate_id",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "candidate_id"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "214",
                    "name": "dlv - alert_type",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "alert_type"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "215",
                    "name": "dlv - lead_action",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "lead_action"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "216",
                    "name": "dlv - user_location",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "user_location"}
                    ]
                },
                {
                    "accountId": num_acc,
                    "containerId": num_cnt,
                    "variableId": "217",
                    "name": "dlv - device_type",
                    "type": "v",
                    "parameter": [
                        {"type": "INTEGER", "key": "dataLayerVersion", "value": "2"},
                        {"type": "BOOLEAN", "key": "setDefaultValue", "value": "false"},
                        {"type": "TEMPLATE", "key": "name", "value": "device_type"}
                    ]
                }
            ]
        }
    }

    filename = "gtm_cv_inteligente_container.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(container, f, indent=2, ensure_ascii=False)
    print(f"GTM Container JSON exported to: {filename}")

if __name__ == "__main__":
    generate_gtm_json()
