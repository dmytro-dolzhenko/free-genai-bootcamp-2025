## SpecStory

## Spring Boot Test Error Analysis (2/12/2025, 9:26:19 PM)

_**User**_

Could you please analyze the project and help to fix following errors?

2025-02-12T21:25:28.656Z DEBUG 10112 --- [           main] org.springframework.test.context.cache   : Spring test ApplicationContext cache statistics: [DefaultContextCache@b548f51 size = 2, maxSize = 32, parentContextCount = 0, hitCount = 96, missCount = 3, failureCount = 1]
2025-02-12T21:25:28.657Z  WARN 10112 --- [           main] o.s.test.context.TestContextManager      : Caught exception while allowing TestExecutionListener [org.springframework.test.context.support.DependencyInjectionTestExecutionListener] to prepare test instance [com.langportal.integration.StudyFlowIntegrationTest@71f4aeb6]

java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@16890f00 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@77e1dacd key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@611587f7, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.springframework.beans.factory.support.BeanDefinitionOverrideException: Invalid bean definition with name 'dataSource' defined in class path resource [com/langportal/config/DatabaseConfig.class]: Cannot register bean definition [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=databaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/DatabaseConfig.class]] for bean 'dataSource' since there is already [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=com.langportal.config.TestDatabaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/TestDatabaseConfig.class]] bound.
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.registerBeanDefinition(DefaultListableBeanFactory.java:1017) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForBeanMethod(ConfigurationClassBeanDefinitionReader.java:277) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForConfigurationClass(ConfigurationClassBeanDefinitionReader.java:144) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitions(ConfigurationClassBeanDefinitionReader.java:120) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.processConfigBeanDefinitions(ConfigurationClassPostProcessor.java:428) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.postProcessBeanDefinitionRegistry(ConfigurationClassPostProcessor.java:289) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanDefinitionRegistryPostProcessors(PostProcessorRegistrationDelegate.java:349) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(PostProcessorRegistrationDelegate.java:118) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.invokeBeanFactoryPostProcessors(AbstractApplicationContext.java:789) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:606) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        ... 73 common frames omitted

2025-02-12T21:25:28.667Z DEBUG 10112 --- [           main] .c.s.DirtiesContextTestExecutionListener : After test class: class [StudyFlowIntegrationTest], class annotated with @DirtiesContext [false] with mode [null]
[ERROR] Tests run: 1, Failures: 0, Errors: 1, Skipped: 0, Time elapsed: 0.386 s <<< FAILURE! -- in com.langportal.integration.StudyFlowIntegrationTest
[ERROR] com.langportal.integration.StudyFlowIntegrationTest.completeStudyFlow -- Time elapsed: 0.001 s <<< ERROR!
java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@16890f00 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@77e1dacd key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@611587f7, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180)
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97)
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260)
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163)
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197)
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179)
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708)
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509)
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499)
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734)
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762)
        at java.base/java.util.Optional.orElseGet(Optional.java:364)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
Caused by: org.springframework.beans.factory.support.BeanDefinitionOverrideException: Invalid bean definition with name 'dataSource' defined in class path resource [com/langportal/config/DatabaseConfig.class]: Cannot register bean definition [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=databaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/DatabaseConfig.class]] for bean 'dataSource' since there is already [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=com.langportal.config.TestDatabaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/TestDatabaseConfig.class]] bound.
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.registerBeanDefinition(DefaultListableBeanFactory.java:1017)
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForBeanMethod(ConfigurationClassBeanDefinitionReader.java:277)
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForConfigurationClass(ConfigurationClassBeanDefinitionReader.java:144)
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitions(ConfigurationClassBeanDefinitionReader.java:120)
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.processConfigBeanDefinitions(ConfigurationClassPostProcessor.java:428)
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.postProcessBeanDefinitionRegistry(ConfigurationClassPostProcessor.java:289)
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanDefinitionRegistryPostProcessors(PostProcessorRegistrationDelegate.java:349)
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(PostProcessorRegistrationDelegate.java:118)
        at org.springframework.context.support.AbstractApplicationContext.invokeBeanFactoryPostProcessors(AbstractApplicationContext.java:789)
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:606)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146)
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762)
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334)
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46)
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458)
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152)
        ... 17 more

[INFO]
[INFO] Results:
[INFO]
[ERROR] Errors:
[ERROR]   WordControllerTest.getWordById_WhenWordDoesNotExist_ShouldReturn404:83 ┬╗ Servlet Request processing failed: java.lang.RuntimeException: Word not found with id: 1
[ERROR]   StudyFlowIntegrationTest.completeStudyFlow ┬╗ IllegalState Failed to load ApplicationContext for [WebMergedContextConfiguration@16890f00 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@77e1dacd key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@611587f7, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
[INFO]
[ERROR] Tests run: 9, Failures: 0, Errors: 2, Skipped: 0
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  14.110 s
[INFO] Finished at: 2025-02-12T21:25:28Z
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:3.2.3:test (default-test) on project backend-java:
[ERROR]
[ERROR] Please refer to f:\Programming\gen-ai-bootcamp\free-genai-bootcamp-2025\lang-portal\backend-java\target\surefire-reports for the individual test results.
[ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException

---

_**Assistant**_

Based on the error logs, there are two main issues:

1. Bean Definition Override Conflict:
The main error is a conflict between two database configurations trying to define the same bean named 'dataSource'. This is happening because both `DatabaseConfig` and `TestDatabaseConfig` are trying to define a dataSource bean.

2. Word Not Found Error in WordControllerTest

Let's fix these issues one by one:

1. First, let's fix the database configuration conflict:

```java:com/langportal/config/DatabaseConfig.java
@Configuration
@Profile("!test") // Add this to exclude this config during tests
public class DatabaseConfig {
    // ... existing code ...
}
```

```java:com/langportal/config/TestDatabaseConfig.java
@Configuration
@Profile("test") // Make sure this is present
public class TestDatabaseConfig {
    // ... existing code ...
}
```

2. For the WordControllerTest error, we need to ensure proper test data setup:

```java:com/langportal/controller/WordControllerTest.java
@WebMvcTest(WordController.class)
public class WordControllerTest {
    @MockBean
    private WordService wordService;
    
    @Test
    public void getWordById_WhenWordDoesNotExist_ShouldReturn404() throws Exception {
        // Given
        when(wordService.getWordById(1L)).thenThrow(new ResourceNotFoundException("Word not found with id: 1"));
        
        // When & Then
        mockMvc.perform(get("/api/words/1"))
               .andExpect(status().isNotFound())
               .andExpect(jsonPath("$.message").value("Word not found with id: 1"));
    }
    
    // ... other test methods ...
}
```

3. Make sure your test class is properly configured:

```java:com/langportal/integration/StudyFlowIntegrationTest.java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("test")
public class StudyFlowIntegrationTest {
    // ... test methods ...
}
```

4. Also, ensure your application.properties/yml for test profile is properly configured:

```properties:src/test/resources/application-test.properties
spring.datasource.url=jdbc:h2:mem:testdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.database-platform=org.hibernate.dialect.H2Dialect
```

These changes should resolve the configuration conflicts and test failures. The key points are:

1. Using @Profile annotations to separate production and test configurations
2. Properly setting up test configurations with @ActiveProfiles
3. Ensuring proper exception handling in controller tests
4. Having separate test properties file

After making these changes, run your tests again with:

```bash
mvn clean test
```

This should resolve the bean definition conflicts and test failures.

---

_**User**_

I don't want to use h2 for testing, please use sqllite3 instead

---

_**Assistant**_

I'll help you modify the configuration to use SQLite instead of H2 for testing.

Let's update the test configuration:

```properties:src/test/resources/application-test.properties
# Test Database Configuration
spring.datasource.url=jdbc:sqlite:memory:testdb?cache=shared
spring.datasource.driver-class-name=org.sqlite.JDBC
spring.datasource.username=sa
spring.datasource.password=

# JPA Configuration
spring.jpa.database-platform=org.hibernate.dialect.SQLiteDialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.generate-ddl=true
spring.jpa.defer-datasource-initialization=true
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.SQLiteDialect
spring.jpa.properties.hibernate.id.new_generator_mappings=false

# Disable Flyway for tests
spring.flyway.enabled=false

# Logging
logging.level.org.hibernate.SQL=DEBUG
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE
logging.level.org.springframework.test=DEBUG
logging.level.org.springframework.security=DEBUG
```

Also, make sure you have the SQLite dependency in your pom.xml:

```xml:pom.xml
<dependency>
    <groupId>org.xerial</groupId>
    <artifactId>sqlite-jdbc</artifactId>
    <version>3.45.1.0</version>
    <scope>test</scope>
</dependency>
<dependency>
    <groupId>org.hibernate.orm</groupId>
    <artifactId>hibernate-community-dialects</artifactId>
    <scope>test</scope>
</dependency>
```

The rest of your test configuration files (DatabaseConfig.java, TestDatabaseConfig.java, etc.) should work fine with these changes. The key differences are:

1. Using SQLite JDBC driver instead of H2
2. Using SQLite dialect instead of H2 dialect
3. Using SQLite in-memory database URL format

This should maintain the same functionality while using SQLite instead of H2 for your tests.

---

_**User**_

I still have these failures

***************************
APPLICATION FAILED TO START
***************************

Description:

The bean 'dataSource', defined in class path resource [com/langportal/config/DatabaseConfig.class], could not be registered. A bean with that name has already been defined in class path resource [com/langportal/config/TestDatabaseConfig.class] and overriding is disabled.

Action:

Consider renaming one of the beans or enabling overriding by setting spring.main.allow-bean-definition-overriding=true




============================
CONDITIONS EVALUATION REPORT
============================


Positive matches:
-----------------

    None


Negative matches:
-----------------

    None


Exclusions:
-----------

    None


Unconditional classes:
----------------------

    None



2025-02-12T21:28:11.870Z DEBUG 1308 --- [           main] org.springframework.test.context.cache   : Spring test ApplicationContext cache statistics: [DefaultContextCache@690677de size = 2, maxSize = 32, parentContextCount = 0, hitCount = 96, missCount = 3, failureCount = 1]
2025-02-12T21:28:11.870Z  WARN 1308 --- [           main] o.s.test.context.TestContextManager      : Caught exception while allowing TestExecutionListener [org.springframework.test.context.support.DependencyInjectionTestExecutionListener] to prepare test instance [com.langportal.integration.StudyFlowIntegrationTest@1c5d376c]

java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@eebd983 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@7a0f43dc key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@3d8bd881, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.springframework.beans.factory.support.BeanDefinitionOverrideException: Invalid bean definition with name 'dataSource' defined in class path resource [com/langportal/config/DatabaseConfig.class]: Cannot register bean definition [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=databaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/DatabaseConfig.class]] for bean 'dataSource' since there is already [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=com.langportal.config.TestDatabaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/TestDatabaseConfig.class]] bound.
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.registerBeanDefinition(DefaultListableBeanFactory.java:1017) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForBeanMethod(ConfigurationClassBeanDefinitionReader.java:277) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForConfigurationClass(ConfigurationClassBeanDefinitionReader.java:144) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitions(ConfigurationClassBeanDefinitionReader.java:120) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.processConfigBeanDefinitions(ConfigurationClassPostProcessor.java:428) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.postProcessBeanDefinitionRegistry(ConfigurationClassPostProcessor.java:289) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanDefinitionRegistryPostProcessors(PostProcessorRegistrationDelegate.java:349) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(PostProcessorRegistrationDelegate.java:118) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.invokeBeanFactoryPostProcessors(AbstractApplicationContext.java:789) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:606) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        ... 73 common frames omitted

2025-02-12T21:28:11.880Z DEBUG 1308 --- [           main] .c.s.DirtiesContextTestExecutionListener : After test class: class [StudyFlowIntegrationTest], class annotated with @DirtiesContext [false] with mode [null]
[ERROR] Tests run: 1, Failures: 0, Errors: 1, Skipped: 0, Time elapsed: 0.405 s <<< FAILURE! -- in com.langportal.integration.StudyFlowIntegrationTest
[ERROR] com.langportal.integration.StudyFlowIntegrationTest.completeStudyFlow -- Time elapsed: 0.002 s <<< ERROR!
java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@eebd983 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@7a0f43dc key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@3d8bd881, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180)
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97)
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260)
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163)
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197)
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179)
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708)
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509)
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499)
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734)
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762)
        at java.base/java.util.Optional.orElseGet(Optional.java:364)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
Caused by: org.springframework.beans.factory.support.BeanDefinitionOverrideException: Invalid bean definition with name 'dataSource' defined in class path resource [com/langportal/config/DatabaseConfig.class]: Cannot register bean definition [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=databaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/DatabaseConfig.class]] for bean 'dataSource' since there is already [Root bean: class [null]; scope=; abstract=false; lazyInit=null; autowireMode=3; dependencyCheck=0; autowireCandidate=true; primary=false; factoryBeanName=com.langportal.config.TestDatabaseConfig; factoryMethodName=dataSource; initMethodNames=null; destroyMethodNames=[(inferred)]; defined in class path resource [com/langportal/config/TestDatabaseConfig.class]] bound.
        at org.springframework.beans.factory.support.DefaultListableBeanFactory.registerBeanDefinition(DefaultListableBeanFactory.java:1017)
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForBeanMethod(ConfigurationClassBeanDefinitionReader.java:277)
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitionsForConfigurationClass(ConfigurationClassBeanDefinitionReader.java:144)
        at org.springframework.context.annotation.ConfigurationClassBeanDefinitionReader.loadBeanDefinitions(ConfigurationClassBeanDefinitionReader.java:120)
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.processConfigBeanDefinitions(ConfigurationClassPostProcessor.java:428)
        at org.springframework.context.annotation.ConfigurationClassPostProcessor.postProcessBeanDefinitionRegistry(ConfigurationClassPostProcessor.java:289)
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanDefinitionRegistryPostProcessors(PostProcessorRegistrationDelegate.java:349)
        at org.springframework.context.support.PostProcessorRegistrationDelegate.invokeBeanFactoryPostProcessors(PostProcessorRegistrationDelegate.java:118)
        at org.springframework.context.support.AbstractApplicationContext.invokeBeanFactoryPostProcessors(AbstractApplicationContext.java:789)
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:606)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146)
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762)
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334)
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46)
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458)
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152)
        ... 17 more

[INFO]
[INFO] Results:
[INFO]
[ERROR] Errors:
[ERROR]   WordControllerTest.getWordById_WhenWordDoesNotExist_ShouldReturn404:83 ┬╗ Servlet Request processing failed: java.lang.RuntimeException: Word not found with id: 1
[ERROR]   StudyFlowIntegrationTest.completeStudyFlow ┬╗ IllegalState Failed to load ApplicationContext for [WebMergedContextConfiguration@eebd983 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@7a0f43dc key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@3d8bd881, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
[INFO]
[ERROR] Tests run: 9, Failures: 0, Errors: 2, Skipped: 0
[INFO]
[INFO] ------------------------------------------------------------------------
[INFO] BUILD FAILURE
[INFO] ------------------------------------------------------------------------
[INFO] Total time:  13.032 s
[INFO] Finished at: 2025-02-12T21:28:11Z
[INFO] ------------------------------------------------------------------------
[ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:3.2.3:test (default-test) on project backend-java:
[ERROR]
[ERROR] Please refer to f:\Programming\gen-ai-bootcamp\free-genai-bootcamp-2025\lang-portal\backend-java\target\surefire-reports for the individual test results.
[ERROR] Please refer to dump files (if any exist) [date].dump, [date]-jvmRun[N].dump and [date].dumpstream.
[ERROR] -> [Help 1]
[ERROR]
[ERROR] To see the full stack trace of the errors, re-run Maven with the -e switch.
[ERROR] Re-run Maven using the -X switch to enable full debug logging.
[ERROR]
[ERROR] For more information about the errors and possible solutions, please read the following articles:
[ERROR] [Help 1] http://cwiki.apache.org/confluence/display/MAVEN/MojoFailureException

---

_**Assistant**_

The error indicates that both `DatabaseConfig` and `TestDatabaseConfig` are trying to define a bean named 'dataSource', and bean overriding is disabled. Let's fix this by:

1. First, let's see the content of both config files:

```java:com/langportal/config/DatabaseConfig.java
@Configuration
@Profile("!test")
public class DatabaseConfig {
    @Bean
    public DataSource dataSource() {
        // ... existing code ...
    }
} 
```

```java:com/langportal/config/TestDatabaseConfig.java
@Configuration
@Profile("test")
public class TestDatabaseConfig {
    @Bean
    public DataSource dataSource() {
        // ... existing code ...
    }
}
```

2. Add the following property to your application-test.properties to allow bean definition overriding:

```properties:src/test/resources/application-test.properties
# Allow bean definition overriding
spring.main.allow-bean-definition-overriding=true

# Existing properties...
spring.datasource.url=jdbc:sqlite:memory:testdb?cache=shared
spring.datasource.driver-class-name=org.sqlite.JDBC
spring.datasource.username=sa
spring.datasource.password=

# JPA Configuration
spring.jpa.database-platform=org.hibernate.dialect.SQLiteDialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.generate-ddl=true
spring.jpa.defer-datasource-initialization=true
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.SQLiteDialect
spring.jpa.properties.hibernate.id.new_generator_mappings=false
```

3. Make sure your test class is properly configured:

```java:com/langportal/integration/StudyFlowIntegrationTest.java
@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@ActiveProfiles("test")
@TestPropertySource(properties = {
    "spring.main.allow-bean-definition-overriding=true"
})
public class StudyFlowIntegrationTest {
    // ... test methods ...
}
```

The key changes are:
1. Adding `spring.main.allow-bean-definition-overriding=true` to application-test.properties
2. Adding `@TestPropertySource` to explicitly set the property in the test class
3. Making sure both config classes have proper `@Profile` annotations

This should resolve the bean definition conflict while maintaining the separate database configurations for test and production environments.

---

_**User**_

Now getting below errors?

2025-02-12T21:29:11.129Z  INFO 15940 --- [           main] c.l.controller.WordControllerTest        : Started WordControllerTest in 0.429 seconds (process running for 4.994)
[ERROR] Tests run: 4, Failures: 0, Errors: 1, Skipped: 0, Time elapsed: 0.513 s <<< FAILURE! -- in com.langportal.controller.WordControllerTest
[ERROR] com.langportal.controller.WordControllerTest.getWordById_WhenWordDoesNotExist_ShouldReturn404 -- Time elapsed: 0.011 s <<< ERROR!
jakarta.servlet.ServletException: Request processing failed: java.lang.RuntimeException: Word not found with id: 1
        at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1022)
        at org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:903)
        at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:564)
        at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:885)
        at org.springframework.test.web.servlet.TestDispatcherServlet.service(TestDispatcherServlet.java:72)
        at jakarta.servlet.http.HttpServlet.service(HttpServlet.java:658)
        at org.springframework.mock.web.MockFilterChain$ServletFilterProxy.doFilter(MockFilterChain.java:165)
        at org.springframework.mock.web.MockFilterChain.doFilter(MockFilterChain.java:132)
        at org.springframework.web.filter.RequestContextFilter.doFilterInternal(RequestContextFilter.java:100)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
        at org.springframework.test.web.servlet.setup.MockMvcFilterDecorator.doFilter(MockMvcFilterDecorator.java:151)
        at org.springframework.mock.web.MockFilterChain.doFilter(MockFilterChain.java:132)
        at org.springframework.web.filter.FormContentFilter.doFilterInternal(FormContentFilter.java:93)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
        at org.springframework.test.web.servlet.setup.MockMvcFilterDecorator.doFilter(MockMvcFilterDecorator.java:151)
        at org.springframework.mock.web.MockFilterChain.doFilter(MockFilterChain.java:132)
        at org.springframework.web.filter.CharacterEncodingFilter.doFilterInternal(CharacterEncodingFilter.java:201)
        at org.springframework.web.filter.OncePerRequestFilter.doFilter(OncePerRequestFilter.java:116)
        at org.springframework.test.web.servlet.setup.MockMvcFilterDecorator.doFilter(MockMvcFilterDecorator.java:151)
        at org.springframework.mock.web.MockFilterChain.doFilter(MockFilterChain.java:132)
        at org.springframework.test.web.servlet.MockMvc.perform(MockMvc.java:201)
        at com.langportal.controller.WordControllerTest.getWordById_WhenWordDoesNotExist_ShouldReturn404(WordControllerTest.java:83)
        at java.base/java.lang.reflect.Method.invoke(Method.java:580)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
Caused by: java.lang.RuntimeException: Word not found with id: 1
        at com.langportal.service.WordService.getWordById(WordService.java:21)
        at com.langportal.controller.WordController.getWordById(WordController.java:29)
        at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
        at java.base/java.lang.reflect.Method.invoke(Method.java:580)
        at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:262)
        at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:190)
        at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:118)
        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:917)
        at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:829)
        at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)
        at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1089)
        at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:979)
        at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1014)
        ... 24 more

[INFO] Running com.langportal.integration.StudyFlowIntegrationTest

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.1)

2025-02-12T21:29:11.280Z  INFO 15940 --- [           main] c.l.i.StudyFlowIntegrationTest           : Starting StudyFlowIntegrationTest using Java 21.0.6 with PID 15940 (started by come_ in f:\Programming\gen-ai-bootcamp\free-genai-bootcamp-2025\lang-portal\backend-java)
2025-02-12T21:29:11.280Z  INFO 15940 --- [           main] c.l.i.StudyFlowIntegrationTest           : The following 1 profile is active: "test"
2025-02-12T21:29:11.740Z  INFO 15940 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
2025-02-12T21:29:11.818Z  INFO 15940 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 68 ms. Found 6 JPA repository interfaces.
2025-02-12T21:29:12.276Z  INFO 15940 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 0 (http)
2025-02-12T21:29:12.291Z  INFO 15940 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2025-02-12T21:29:12.292Z  INFO 15940 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.17]
2025-02-12T21:29:12.386Z  INFO 15940 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2025-02-12T21:29:12.386Z  INFO 15940 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1104 ms
2025-02-12T21:29:12.535Z  INFO 15940 --- [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2025-02-12T21:29:12.621Z  INFO 15940 --- [           main] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 6.4.1.Final
2025-02-12T21:29:12.674Z  INFO 15940 --- [           main] o.h.c.internal.RegionFactoryInitiator    : HHH000026: Second-level cache disabled
2025-02-12T21:29:12.810Z  INFO 15940 --- [           main] o.s.o.j.p.SpringPersistenceUnitInfo      : No LoadTimeWeaver setup: ignoring JPA class transformer
2025-02-12T21:29:13.013Z  WARN 15940 --- [           main] o.h.e.j.e.i.JdbcEnvironmentInitiator     : HHH000342: Could not obtain connection to query metadata

org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:328) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:277) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.WorkExecutor.executeReturningWork(WorkExecutor.java:58) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.AbstractReturningWork.accept(AbstractReturningWork.java:34) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.resource.transaction.backend.jdbc.internal.JdbcIsolationDelegate.delegateWork(JdbcIsolationDelegate.java:70) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [org.hibernate.dialect.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 124 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : org.hibernate.dialect.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 125 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted

2025-02-12T21:29:13.020Z ERROR 15940 --- [           main] j.LocalContainerEntityManagerFactoryBean : Failed to initialize JPA EntityManagerFactory: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:29:13.021Z  WARN 15940 --- [           main] ConfigServletWebServerApplicationContext : Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:29:13.022Z  INFO 15940 --- [           main] o.apache.catalina.core.StandardService   : Stopping service [Tomcat]
2025-02-12T21:29:13.032Z  INFO 15940 --- [           main] .s.b.a.l.ConditionEvaluationReportLogger :

Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2025-02-12T21:29:13.050Z ERROR 15940 --- [           main] o.s.boot.SpringApplication               : Application run failed

org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        ... 95 common frames omitted
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 110 common frames omitted
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [org.hibernate.dialect.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 120 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : org.hibernate.dialect.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 121 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted




============================
CONDITIONS EVALUATION REPORT
============================


Positive matches:
-----------------

    None


Negative matches:
-----------------

    None


Exclusions:
-----------

    None


Unconditional classes:
----------------------

    None



2025-02-12T21:29:13.063Z DEBUG 15940 --- [           main] org.springframework.test.context.cache   : Spring test ApplicationContext cache statistics: [DefaultContextCache@3df7e309 size = 2, maxSize = 32, parentContextCount = 0, hitCount = 96, missCount = 3, failureCount = 1]
2025-02-12T21:29:13.063Z  WARN 15940 --- [           main] o.s.test.context.TestContextManager      : Caught exception while allowing TestExecutionListener [org.springframework.test.context.support.DependencyInjectionTestExecutionListener] to prepare test instance [com.langportal.integration.StudyFlowIntegrationTest@55f4ec04]

java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@3ac76ad9 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@213c812a key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@2cdcfaa6, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        ... 73 common frames omitted
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        ... 95 common frames omitted
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 110 common frames omitted
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [org.hibernate.dialect.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 120 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : org.hibernate.dialect.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 121 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted

2025-02-12T21:29:13.075Z DEBUG 15940 --- [           main] .c.s.DirtiesContextTestExecutionListener : After test class: class [StudyFlowIntegrationTest], class annotated with @DirtiesContext [false] with mode [null]
[ERROR] Tests run: 1, Failures: 0, Errors: 1, Skipped: 0, Time elapsed: 1.881 s <<< FAILURE! -- in com.langportal.integration.StudyFlowIntegrationTest
[ERROR] com.langportal.integration.StudyFlowIntegrationTest.completeStudyFlow -- Time elapsed: 0.007 s <<< ERROR!
java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@3ac76ad9 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@213c812a key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@2cdcfaa6, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180)
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97)
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260)
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163)
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197)
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179)
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708)
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509)
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499)
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734)
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762)
        at java.base/java.util.Optional.orElseGet(Optional.java:364)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521)
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232)
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950)
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146)
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762)
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334)
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46)
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458)
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152)
        ... 17 more
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276)
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238)
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215)
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45)
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223)
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191)
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170)
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432)
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503)
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75)
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376)
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409)
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396)
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769)
        ... 39 more
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154)
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236)
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189)
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123)
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68)
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129)
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263)
        ... 54 more
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [org.hibernate.dialect.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126)
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150)
        ... 64 more
Caused by: java.lang.ClassNotFoundException: Could not load requested class : org.hibernate.dialect.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
        at java.base/java.lang.Class.forName0(Native Method)
        at java.base/java.lang.Class.forName(Class.java:534)
        at java.base/java.lang.Class.forName(Class.java:513)
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123)
        ... 65 more
Caused by: java.lang.Throwable
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209)
        ... 71 more
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206)
                ... 71 more
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206)
                ... 71 more
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206)
                ... 71 more

[INFO]
[INFO] Results:
[INFO]
[ERROR] Errors:
[ERROR]   WordControllerTest.getWordById_WhenWordDoesNotExist_ShouldReturn404:83 ┬╗ Servlet Request processing failed: java.lang.RuntimeException: Word not found with id: 1
[ERROR]   StudyFlowIntegrationTest.completeStudyFlow ┬╗ IllegalState Failed to load ApplicationContext for [WebMergedContextConfiguration@3ac76ad9 testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@213c812a key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@2cdcfaa6, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
[INFO]
[ERROR] Tests run: 9, Failures: 0, Errors: 2, Skipped: 0

---

_**Assistant**_

The errors indicate two main issues:

1. SQLite dialect not found - we need to create a custom SQLite dialect for Hibernate 6
2. Word not found exception in the controller test

Let's fix these issues:

1. First, let's create a custom SQLite dialect:

```java:com/langportal/config/SQLiteDialect.java
package com.langportal.config;

import org.hibernate.dialect.Dialect;
import org.hibernate.dialect.function.SQLFunctionTemplate;
import org.hibernate.dialect.function.StandardSQLFunction;
import org.hibernate.dialect.function.VarArgsSQLFunction;
import org.hibernate.dialect.identity.IdentityColumnSupport;
import org.hibernate.dialect.identity.IdentityColumnSupportImpl;
import org.hibernate.dialect.pagination.LimitHandler;
import org.hibernate.dialect.pagination.LimitOffsetLimitHandler;
import org.hibernate.engine.spi.SessionFactoryImplementor;
import org.hibernate.type.StandardBasicTypes;

import java.sql.Types;

public class SQLiteDialect extends Dialect {

    public SQLiteDialect() {
        registerColumnType(Types.BIT, "integer");
        registerColumnType(Types.TINYINT, "tinyint");
        registerColumnType(Types.SMALLINT, "smallint");
        registerColumnType(Types.INTEGER, "integer");
        registerColumnType(Types.BIGINT, "bigint");
        registerColumnType(Types.FLOAT, "float");
        registerColumnType(Types.REAL, "real");
        registerColumnType(Types.DOUBLE, "double");
        registerColumnType(Types.NUMERIC, "numeric");
        registerColumnType(Types.DECIMAL, "decimal");
        registerColumnType(Types.CHAR, "char");
        registerColumnType(Types.VARCHAR, "varchar");
        registerColumnType(Types.LONGVARCHAR, "longvarchar");
        registerColumnType(Types.DATE, "date");
        registerColumnType(Types.TIME, "time");
        registerColumnType(Types.TIMESTAMP, "timestamp");
        registerColumnType(Types.BINARY, "blob");
        registerColumnType(Types.VARBINARY, "blob");
        registerColumnType(Types.LONGVARBINARY, "blob");
        registerColumnType(Types.BLOB, "blob");
        registerColumnType(Types.CLOB, "clob");
        registerColumnType(Types.BOOLEAN, "integer");

        registerFunction("concat", new VarArgsSQLFunction(StandardBasicTypes.STRING, "", "||", ""));
        registerFunction("mod", new SQLFunctionTemplate(StandardBasicTypes.INTEGER, "?1 % ?2"));
        registerFunction("substr", new StandardSQLFunction("substr", StandardBasicTypes.STRING));
        registerFunction("substring", new StandardSQLFunction("substr", StandardBasicTypes.STRING));
    }

    @Override
    public IdentityColumnSupport getIdentityColumnSupport() {
        return new SQLiteIdentityColumnSupport();
    }

    @Override
    public boolean supportsIdentityColumns() {
        return true;
    }

    @Override
    public boolean hasDataTypeInIdentityColumn() {
        return false;
    }

    @Override
    public String getSelectGUIDString() {
        return "select hex(randomblob(16))";
    }

    @Override
    public boolean supportsLimit() {
        return true;
    }

    @Override
    protected LimitHandler getLimitHandler() {
        return new LimitOffsetLimitHandler(this);
    }

    @Override
    public boolean supportsTemporaryTables() {
        return true;
    }

    @Override
    public String getCreateTemporaryTableString() {
        return "create temporary table if not exists";
    }

    @Override
    public boolean dropTemporaryTableAfterUse() {
        return false;
    }

    @Override
    public boolean supportsCurrentTimestampSelection() {
        return true;
    }

    @Override
    public boolean isCurrentTimestampSelectStringCallable() {
        return false;
    }

    @Override
    public String getCurrentTimestampSelectString() {
        return "select current_timestamp";
    }

    @Override
    public boolean supportsUnionAll() {
        return true;
    }

    @Override
    public boolean hasAlterTable() {
        return false;
    }

    @Override
    public boolean dropConstraints() {
        return false;
    }

    @Override
    public String getForUpdateString() {
        return "";
    }

    @Override
    public String getAddColumnString() {
        return "add column";
    }

    @Override
    public boolean supportsOuterJoinForUpdate() {
        return false;
    }

    private static class SQLiteIdentityColumnSupport extends IdentityColumnSupportImpl {
        @Override
        public boolean supportsIdentityColumns() {
            return true;
        }

        @Override
        public String getIdentitySelectString(String table, String column, int type) {
            return "select last_insert_rowid()";
        }

        @Override
        public String getIdentityColumnString(int type) {
            return "integer";
        }
    }
}
```

2. Update the application-test.properties to use our custom dialect:

```properties:src/test/resources/application-test.properties
# Test Database Configuration
spring.datasource.url=jdbc:sqlite:memory:testdb?cache=shared
spring.datasource.driver-class-name=org.sqlite.JDBC
spring.datasource.username=sa
spring.datasource.password=

# JPA Configuration
spring.jpa.database-platform=com.langportal.config.SQLiteDialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.generate-ddl=true
spring.jpa.defer-datasource-initialization=true
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=com.langportal.config.SQLiteDialect
spring.jpa.properties.hibernate.id.new_generator_mappings=false

# Allow bean definition overriding
spring.main.allow-bean-definition-overriding=true
```

3. For the WordControllerTest error, we need to properly handle the ResourceNotFoundException:

```java:com/langportal/controller/WordControllerTest.java
@WebMvcTest(WordController.class)
public class WordControllerTest {
    @MockBean
    private WordService wordService;
    
    @Autowired
    private MockMvc mockMvc;
    
    @Test
    public void getWordById_WhenWordDoesNotExist_ShouldReturn404() throws Exception {
        // Given
        when(wordService.getWordById(1L)).thenThrow(new ResourceNotFoundException("Word not found with id: 1"));
        
        // When & Then
        mockMvc.perform(get("/api/words/1"))
               .andExpect(status().isNotFound())
               .andExpect(jsonPath("$.message").value("Word not found with id: 1"));
    }
}
```

Make sure your WordController properly handles the ResourceNotFoundException with a @ExceptionHandler:

```java:com/langportal/controller/WordController.java
@RestController
@RequestMapping("/api/words")
public class WordController {
    
    @ExceptionHandler(ResourceNotFoundException.class)
    @ResponseStatus(HttpStatus.NOT_FOUND)
    public ResponseEntity<Map<String, String>> handleResourceNotFoundException(ResourceNotFoundException ex) {
        Map<String, String> response = new HashMap<>();
        response.put("message", ex.getMessage());
        return ResponseEntity.status(HttpStatus.NOT_FOUND).body(response);
    }
    
    // ... other methods
}
```

These changes should resolve both the SQLite dialect issue and the controller test failure.

---

_**User**_

025-02-12T21:30:57.486Z  WARN 20916 --- [           main] o.h.e.j.e.i.JdbcEnvironmentInitiator     : HHH000342: Could not obtain connection to query metadata

org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:328) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:277) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.WorkExecutor.executeReturningWork(WorkExecutor.java:58) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.AbstractReturningWork.accept(AbstractReturningWork.java:34) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.resource.transaction.backend.jdbc.internal.JdbcIsolationDelegate.delegateWork(JdbcIsolationDelegate.java:70) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [com.langportal.config.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 124 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : com.langportal.config.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 125 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted

2025-02-12T21:30:57.493Z ERROR 20916 --- [           main] j.LocalContainerEntityManagerFactoryBean : Failed to initialize JPA EntityManagerFactory: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:30:57.493Z  WARN 20916 --- [           main] ConfigServletWebServerApplicationContext : Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:30:57.494Z  INFO 20916 --- [           main] o.apache.catalina.core.StandardService   : Stopping service [Tomcat]
2025-02-12T21:30:57.504Z  INFO 20916 --- [           main] .s.b.a.l.ConditionEvaluationReportLogger :

Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2025-02-12T21:30:57.526Z ERROR 20916 --- [           main] o.s.boot.SpringApplication               : Application run failed

org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        ... 95 common frames omitted
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 110 common frames omitted
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [com.langportal.config.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 120 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : com.langportal.config.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 121 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted

---

_**Assistant**_

The error indicates that Hibernate cannot find the SQLiteDialect class. This is because we need to update our SQLiteDialect class to be compatible with Hibernate 6. Let's modify the SQLiteDialect class:

```java:com/langportal/config/SQLiteDialect.java
package com.langportal.config;

import org.hibernate.dialect.DatabaseVersion;
import org.hibernate.dialect.Dialect;
import org.hibernate.dialect.function.SQLFunctionTemplate;
import org.hibernate.dialect.function.StandardSQLFunction;
import org.hibernate.dialect.function.VarArgsSQLFunction;
import org.hibernate.dialect.identity.IdentityColumnSupport;
import org.hibernate.dialect.identity.IdentityColumnSupportImpl;
import org.hibernate.dialect.pagination.LimitHandler;
import org.hibernate.dialect.pagination.LimitOffsetLimitHandler;
import org.hibernate.engine.jdbc.dialect.spi.DialectResolutionInfo;
import org.hibernate.type.StandardBasicTypes;

import java.sql.Types;

public class SQLiteDialect extends Dialect {

    public SQLiteDialect() {
        super(DatabaseVersion.make(3, 0));
        registerColumnType(Types.BIT, "integer");
        registerColumnType(Types.TINYINT, "tinyint");
        registerColumnType(Types.SMALLINT, "smallint");
        registerColumnType(Types.INTEGER, "integer");
        registerColumnType(Types.BIGINT, "bigint");
        registerColumnType(Types.FLOAT, "float");
        registerColumnType(Types.REAL, "real");
        registerColumnType(Types.DOUBLE, "double");
        registerColumnType(Types.NUMERIC, "numeric");
        registerColumnType(Types.DECIMAL, "decimal");
        registerColumnType(Types.CHAR, "char");
        registerColumnType(Types.VARCHAR, "varchar");
        registerColumnType(Types.LONGVARCHAR, "longvarchar");
        registerColumnType(Types.DATE, "date");
        registerColumnType(Types.TIME, "time");
        registerColumnType(Types.TIMESTAMP, "timestamp");
        registerColumnType(Types.BINARY, "blob");
        registerColumnType(Types.VARBINARY, "blob");
        registerColumnType(Types.LONGVARBINARY, "blob");
        registerColumnType(Types.BLOB, "blob");
        registerColumnType(Types.CLOB, "clob");
        registerColumnType(Types.BOOLEAN, "integer");

        registerFunction("concat", new VarArgsSQLFunction(StandardBasicTypes.STRING, "", "||", ""));
        registerFunction("mod", new SQLFunctionTemplate(StandardBasicTypes.INTEGER, "?1 % ?2"));
        registerFunction("substr", new StandardSQLFunction("substr", StandardBasicTypes.STRING));
        registerFunction("substring", new StandardSQLFunction("substr", StandardBasicTypes.STRING));
    }

    @Override
    public IdentityColumnSupport getIdentityColumnSupport() {
        return new SQLiteIdentityColumnSupport();
    }

    @Override
    public boolean supportsIdentityColumns() {
        return true;
    }

    @Override
    public boolean hasDataTypeInIdentityColumn() {
        return false;
    }

    @Override
    public String getSelectGUIDString() {
        return "select hex(randomblob(16))";
    }

    @Override
    public boolean supportsLimit() {
        return true;
    }

    @Override
    protected LimitHandler getLimitHandler() {
        return new LimitOffsetLimitHandler(this);
    }

    @Override
    public boolean supportsTemporaryTables() {
        return true;
    }

    @Override
    public String getCreateTemporaryTableString() {
        return "create temporary table if not exists";
    }

    @Override
    public boolean dropTemporaryTableAfterUse() {
        return false;
    }

    @Override
    public boolean supportsCurrentTimestampSelection() {
        return true;
    }

    @Override
    public boolean isCurrentTimestampSelectStringCallable() {
        return false;
    }

    @Override
    public String getCurrentTimestampSelectString() {
        return "select current_timestamp";
    }

    @Override
    public boolean supportsUnionAll() {
        return true;
    }

    @Override
    public boolean hasAlterTable() {
        return false;
    }

    @Override
    public boolean dropConstraints() {
        return false;
    }

    @Override
    public String getAddColumnString() {
        return "add column";
    }

    @Override
    public boolean supportsOuterJoinForUpdate() {
        return false;
    }

    private static class SQLiteIdentityColumnSupport extends IdentityColumnSupportImpl {
        @Override
        public boolean supportsIdentityColumns() {
            return true;
        }

        @Override
        public String getIdentitySelectString(String table, String column, int type) {
            return "select last_insert_rowid()";
        }

        @Override
        public String getIdentityColumnString(int type) {
            return "integer";
        }
    }
}
```

The main changes are:
1. Added `DatabaseVersion` in the constructor
2. Removed unused imports
3. Updated the class to be compatible with Hibernate 6 dialect structure

This should resolve the ClassNotFoundException for SQLiteDialect. The key change is extending the Hibernate 6 Dialect class properly with the required database version information.

---

_**User**_

[ERROR] Tests run: 1, Failures: 0, Errors: 1, Skipped: 0, Time elapsed: 1.885 s <<< FAILURE! -- in com.langportal.integration.StudyFlowIntegrationTest
[ERROR] com.langportal.integration.StudyFlowIntegrationTest.completeStudyFlow -- Time elapsed: 0.005 s <<< ERROR!
java.lang.IllegalStateException: Failed to load ApplicationContext for [WebMergedContextConfiguration@213c812a testClass = com.langportal.integration.StudyFlowIntegrationTest, locations = [], classes = [com.langportal.LangPortalApplication], contextInitializerClasses = [], activeProfiles = ["test"], propertySourceDescriptors = [], propertySourceProperties = ["org.springframework.boot.test.context.SpringBootTestContextBootstrapper=true", "server.port=0"], contextCustomizers = [[ImportsContextCustomizer@25814d3c key = [com.langportal.config.TestDatabaseConfig]], org.springframework.boot.test.context.filter.ExcludeFilterContextCustomizer@6c372fe6, org.springframework.boot.test.json.DuplicateJsonObjectContextCustomizerFactory$DuplicateJsonObjectContextCustomizer@4167d97b, org.springframework.boot.test.mock.mockito.MockitoContextCustomizer@0, org.springframework.boot.test.web.client.TestRestTemplateContextCustomizer@731ab49b, org.springframework.boot.test.autoconfigure.actuate.observability.ObservabilityContextCustomizerFactory$DisableObservabilityContextCustomizer@1f, org.springframework.boot.test.autoconfigure.properties.PropertyMappingContextCustomizer@0, org.springframework.boot.test.autoconfigure.web.servlet.WebDriverContextCustomizer@3561c410, org.springframework.boot.test.context.SpringBootTestAnnotation@2559bd8d], resourceBasePath = "src/main/webapp", contextLoader = org.springframework.boot.test.context.SpringBootContextLoader, parent = null]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:180)
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141)
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97)
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260)
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163)
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197)
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179)
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708)
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509)
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499)
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735)
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734)
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762)
        at java.base/java.util.Optional.orElseGet(Optional.java:364)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596)
Caused by: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521)
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325)
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234)
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323)
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199)
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232)
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950)
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625)
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146)
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762)
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464)
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334)
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58)
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46)
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458)
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137)
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225)
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152)
        ... 17 more
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276)
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238)
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215)
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45)
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223)
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191)
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170)
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432)
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503)
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75)
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376)
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409)
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396)
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820)
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769)
        ... 39 more
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154)
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236)
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189)
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123)
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107)
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68)
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129)
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263)
        ... 54 more
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [com.langportal.config.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126)
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150)
        ... 64 more
Caused by: java.lang.ClassNotFoundException: Could not load requested class : com.langportal.config.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593)
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
        at java.base/java.lang.Class.forName0(Native Method)
        at java.base/java.lang.Class.forName(Class.java:534)
        at java.base/java.lang.Class.forName(Class.java:513)
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123)
        ... 65 more
Caused by: java.lang.Throwable
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209)
        ... 71 more
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206)
                ... 71 more
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206)
                ... 71 more
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641)
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188)
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526)
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206)
                ... 71 more

[INFO]

---

_**Assistant**_

The error suggests that the SQLiteDialect class is not being found in the classpath during test execution. Let's check the DatabaseConfig and TestDatabaseConfig files to ensure they're properly configured.

Could you show me the contents of:
1. `com/langportal/config/DatabaseConfig.java`
2. `com/langportal/config/TestDatabaseConfig.java`

In the meantime, let's try updating the SQLiteDialect class to make it more discoverable by Hibernate:

```java:com/langportal/config/SQLiteDialect.java
package com.langportal.config;

import org.hibernate.dialect.DatabaseVersion;
import org.hibernate.dialect.Dialect;
import org.hibernate.dialect.function.SQLFunctionTemplate;
import org.hibernate.dialect.function.StandardSQLFunction;
import org.hibernate.dialect.function.VarArgsSQLFunction;
import org.hibernate.dialect.identity.IdentityColumnSupport;
import org.hibernate.dialect.identity.IdentityColumnSupportImpl;
import org.hibernate.dialect.pagination.LimitHandler;
import org.hibernate.dialect.pagination.LimitOffsetLimitHandler;
import org.hibernate.engine.jdbc.dialect.spi.DialectResolutionInfo;
import org.hibernate.type.StandardBasicTypes;

import java.sql.Types;

public class SQLiteDialect extends Dialect {

    public SQLiteDialect() {
        this(DatabaseVersion.make(3, 0));
    }

    public SQLiteDialect(final DatabaseVersion version) {
        super(version);
        registerColumnType(Types.BIT, "integer");
        registerColumnType(Types.TINYINT, "tinyint");
        registerColumnType(Types.SMALLINT, "smallint");
        registerColumnType(Types.INTEGER, "integer");
        registerColumnType(Types.BIGINT, "bigint");
        registerColumnType(Types.FLOAT, "float");
        registerColumnType(Types.REAL, "real");
        registerColumnType(Types.DOUBLE, "double");
        registerColumnType(Types.NUMERIC, "numeric");
        registerColumnType(Types.DECIMAL, "decimal");
        registerColumnType(Types.CHAR, "char");
        registerColumnType(Types.VARCHAR, "varchar");
        registerColumnType(Types.LONGVARCHAR, "longvarchar");
        registerColumnType(Types.DATE, "date");
        registerColumnType(Types.TIME, "time");
        registerColumnType(Types.TIMESTAMP, "timestamp");
        registerColumnType(Types.BINARY, "blob");
        registerColumnType(Types.VARBINARY, "blob");
        registerColumnType(Types.LONGVARBINARY, "blob");
        registerColumnType(Types.BLOB, "blob");
        registerColumnType(Types.CLOB, "clob");
        registerColumnType(Types.BOOLEAN, "integer");

        registerFunction("concat", new VarArgsSQLFunction(StandardBasicTypes.STRING, "", "||", ""));
        registerFunction("mod", new SQLFunctionTemplate(StandardBasicTypes.INTEGER, "?1 % ?2"));
        registerFunction("substr", new StandardSQLFunction("substr", StandardBasicTypes.STRING));
        registerFunction("substring", new StandardSQLFunction("substr", StandardBasicTypes.STRING));
    }

    public String getDialectName() {
        return "SQLite";
    }

    @Override
    public IdentityColumnSupport getIdentityColumnSupport() {
        return new SQLiteIdentityColumnSupport();
    }

    @Override
    public boolean supportsIdentityColumns() {
        return true;
    }

    @Override
    public boolean hasDataTypeInIdentityColumn() {
        return false;
    }

    @Override
    public String getSelectGUIDString() {
        return "select hex(randomblob(16))";
    }

    @Override
    public boolean supportsLimit() {
        return true;
    }

    @Override
    protected LimitHandler getLimitHandler() {
        return new LimitOffsetLimitHandler(this);
    }

    @Override
    public boolean supportsTemporaryTables() {
        return true;
    }

    @Override
    public String getCreateTemporaryTableString() {
        return "create temporary table if not exists";
    }

    @Override
    public boolean dropTemporaryTableAfterUse() {
        return false;
    }

    @Override
    public boolean supportsCurrentTimestampSelection() {
        return true;
    }

    @Override
    public boolean isCurrentTimestampSelectStringCallable() {
        return false;
    }

    @Override
    public String getCurrentTimestampSelectString() {
        return "select current_timestamp";
    }

    @Override
    public boolean supportsUnionAll() {
        return true;
    }

    @Override
    public boolean hasAlterTable() {
        return false;
    }

    @Override
    public boolean dropConstraints() {
        return false;
    }

    @Override
    public String getAddColumnString() {
        return "add column";
    }

    @Override
    public boolean supportsOuterJoinForUpdate() {
        return false;
    }

    private static class SQLiteIdentityColumnSupport extends IdentityColumnSupportImpl {
        @Override
        public boolean supportsIdentityColumns() {
            return true;
        }

        @Override
        public String getIdentitySelectString(String table, String column, int type) {
            return "select last_insert_rowid()";
        }

        @Override
        public String getIdentityColumnString(int type) {
            return "integer";
        }
    }
}
```

The main changes are:
1. Added a constructor that takes DatabaseVersion
2. Added getDialectName() method
3. Restructured the constructors to be more Hibernate 6 friendly

Could you share the contents of the database configuration files? That would help identify if there are any configuration issues preventing the dialect from being discovered.

---

_**User**_

[INFO] Running com.langportal.integration.StudyFlowIntegrationTest

  .   ____          _            __ _ _
 /\\ / ___'_ __ _ _(_)_ __  __ _ \ \ \ \
( ( )\___ | '_ | '_| | '_ \/ _` | \ \ \ \
 \\/  ___)| |_)| | | | | || (_| |  ) ) ) )
  '  |____| .__|_| |_|_| |_\__, | / / / /
 =========|_|==============|___/=/_/_/_/
 :: Spring Boot ::                (v3.2.1)

2025-02-12T21:33:16.617Z  INFO 4856 --- [           main] c.l.i.StudyFlowIntegrationTest           : Starting StudyFlowIntegrationTest using Java 21.0.6 with PID 4856 (started by come_ in f:\Programming\gen-ai-bootcamp\free-genai-bootcamp-2025\lang-portal\backend-java)
2025-02-12T21:33:16.618Z  INFO 4856 --- [           main] c.l.i.StudyFlowIntegrationTest           : The following 1 profile is active: "test"
2025-02-12T21:33:17.067Z  INFO 4856 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Bootstrapping Spring Data JPA repositories in DEFAULT mode.
2025-02-12T21:33:17.144Z  INFO 4856 --- [           main] .s.d.r.c.RepositoryConfigurationDelegate : Finished Spring Data repository scanning in 66 ms. Found 6 JPA repository interfaces.
2025-02-12T21:33:17.616Z  INFO 4856 --- [           main] o.s.b.w.embedded.tomcat.TomcatWebServer  : Tomcat initialized with port 0 (http)
2025-02-12T21:33:17.634Z  INFO 4856 --- [           main] o.apache.catalina.core.StandardService   : Starting service [Tomcat]
2025-02-12T21:33:17.634Z  INFO 4856 --- [           main] o.apache.catalina.core.StandardEngine    : Starting Servlet engine: [Apache Tomcat/10.1.17]
2025-02-12T21:33:17.735Z  INFO 4856 --- [           main] o.a.c.c.C.[Tomcat].[localhost].[/]       : Initializing Spring embedded WebApplicationContext
2025-02-12T21:33:17.735Z  INFO 4856 --- [           main] w.s.c.ServletWebServerApplicationContext : Root WebApplicationContext: initialization completed in 1115 ms
2025-02-12T21:33:17.887Z  INFO 4856 --- [           main] o.hibernate.jpa.internal.util.LogHelper  : HHH000204: Processing PersistenceUnitInfo [name: default]
2025-02-12T21:33:17.981Z  INFO 4856 --- [           main] org.hibernate.Version                    : HHH000412: Hibernate ORM core version 6.4.1.Final
2025-02-12T21:33:18.037Z  INFO 4856 --- [           main] o.h.c.internal.RegionFactoryInitiator    : HHH000026: Second-level cache disabled
2025-02-12T21:33:18.193Z  INFO 4856 --- [           main] o.s.o.j.p.SpringPersistenceUnitInfo      : No LoadTimeWeaver setup: ignoring JPA class transformer
2025-02-12T21:33:18.343Z  WARN 4856 --- [           main] o.h.e.j.e.i.JdbcEnvironmentInitiator     : HHH000342: Could not obtain connection to query metadata

org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:328) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:277) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.WorkExecutor.executeReturningWork(WorkExecutor.java:58) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.AbstractReturningWork.accept(AbstractReturningWork.java:34) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.resource.transaction.backend.jdbc.internal.JdbcIsolationDelegate.delegateWork(JdbcIsolationDelegate.java:70) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [com.langportal.config.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 124 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : com.langportal.config.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 125 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted

2025-02-12T21:33:18.352Z ERROR 4856 --- [           main] j.LocalContainerEntityManagerFactoryBean : Failed to initialize JPA EntityManagerFactory: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:33:18.352Z  WARN 4856 --- [           main] ConfigServletWebServerApplicationContext : Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:33:18.354Z  INFO 4856 --- [           main] o.apache.catalina.core.StandardService   : Stopping service [Tomcat]
2025-02-12T21:33:18.366Z  INFO 4856 --- [           main] .s.b.a.l.ConditionEvaluationReportLogger :

Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2025-02-12T21:33:18.390Z ERROR 4856 --- [           main] o.s.boot.SpringApplication               : Application run failed

org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        ... 95 common frames omitted
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [com.langportal.config.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 110 common frames omitted
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [com.langportal.config.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 120 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : com.langportal.config.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 121 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: com.langportal.config.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted




============================
CONDITIONS EVALUATION REPORT
============================


---

_**Assistant**_

The error suggests that the SQLiteDialect class is not being found in the classpath. Let's try using Hibernate's built-in SQLite dialect instead of our custom one.

Update the application-test.properties file:

```properties:src/test/resources/application-test.properties
# Test Database Configuration
spring.datasource.url=jdbc:sqlite:memory:testdb?cache=shared
spring.datasource.driver-class-name=org.sqlite.JDBC
spring.datasource.username=sa
spring.datasource.password=

# JPA Configuration
spring.jpa.database-platform=org.hibernate.dialect.SQLiteDialect
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.generate-ddl=true
spring.jpa.defer-datasource-initialization=true
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.format_sql=true
spring.jpa.properties.hibernate.dialect=org.hibernate.dialect.SQLiteDialect
spring.jpa.properties.hibernate.id.new_generator_mappings=false

# Allow bean definition overriding
spring.main.allow-bean-definition-overriding=true

# Disable Flyway for tests
spring.flyway.enabled=false

# Logging
logging.level.org.hibernate.SQL=DEBUG
logging.level.org.hibernate.type.descriptor.sql.BasicBinder=TRACE
logging.level.org.springframework.test=DEBUG
logging.level.org.springframework.security=DEBUG
```

Also, make sure you have the SQLite JDBC driver dependency in your pom.xml:

```xml
<dependency>
    <groupId>org.xerial</groupId>
    <artifactId>sqlite-jdbc</artifactId>
    <version>3.45.1.0</version>
    <scope>test</scope>
</dependency>
```

If you still want to use a custom dialect, we need to make sure the SQLiteDialect class is in the correct package and is being compiled. Could you verify:

1. The location of SQLiteDialect.java (should be in src/main/java/com/langportal/config/)
2. That the file is being compiled (check target/classes/com/langportal/config/ for SQLiteDialect.class)

Let me know if you need me to check anything specific.

---

_**User**_

Could you please help to resolve?


org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:328) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator$1.execute(JdbcEnvironmentInitiator.java:277) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.WorkExecutor.executeReturningWork(WorkExecutor.java:58) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jdbc.AbstractReturningWork.accept(AbstractReturningWork.java:34) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.resource.transaction.backend.jdbc.internal.JdbcIsolationDelegate.delegateWork(JdbcIsolationDelegate.java:70) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [org.hibernate.dialect.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 124 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : org.hibernate.dialect.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 125 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 131 common frames omitted

2025-02-12T21:34:30.049Z ERROR 19512 --- [           main] j.LocalContainerEntityManagerFactoryBean : Failed to initialize JPA EntityManagerFactory: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:34:30.049Z  WARN 19512 --- [           main] ConfigServletWebServerApplicationContext : Exception encountered during context initialization - cancelling refresh attempt: org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
2025-02-12T21:34:30.051Z  INFO 19512 --- [           main] o.apache.catalina.core.StandardService   : Stopping service [Tomcat]
2025-02-12T21:34:30.063Z  INFO 19512 --- [           main] .s.b.a.l.ConditionEvaluationReportLogger :

Error starting ApplicationContext. To display the condition evaluation report re-run your application with 'debug' enabled.
2025-02-12T21:34:30.088Z ERROR 19512 --- [           main] o.s.boot.SpringApplication               : Application run failed

org.springframework.beans.factory.BeanCreationException: Error creating bean with name 'entityManagerFactory' defined in class path resource [org/springframework/boot/autoconfigure/orm/jpa/HibernateJpaConfiguration.class]: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1773) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.doCreateBean(AbstractAutowireCapableBeanFactory.java:599) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.createBean(AbstractAutowireCapableBeanFactory.java:521) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.lambda$doGetBean$0(AbstractBeanFactory.java:325) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.DefaultSingletonBeanRegistry.getSingleton(DefaultSingletonBeanRegistry.java:234) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.doGetBean(AbstractBeanFactory.java:323) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractBeanFactory.getBean(AbstractBeanFactory.java:199) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.getBean(AbstractApplicationContext.java:1232) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.finishBeanFactoryInitialization(AbstractApplicationContext.java:950) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.context.support.AbstractApplicationContext.refresh(AbstractApplicationContext.java:625) ~[spring-context-6.1.2.jar:6.1.2]
        at org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext.refresh(ServletWebServerApplicationContext.java:146) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refresh(SpringApplication.java:762) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.refreshContext(SpringApplication.java:464) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.SpringApplication.run(SpringApplication.java:334) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.lambda$loadContext$3(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:58) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.util.function.ThrowingSupplier.get(ThrowingSupplier.java:46) ~[spring-core-6.1.2.jar:6.1.2]
        at org.springframework.boot.SpringApplication.withHook(SpringApplication.java:1458) ~[spring-boot-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader$ContextLoaderHook.run(SpringBootContextLoader.java:552) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:137) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.boot.test.context.SpringBootContextLoader.loadContext(SpringBootContextLoader.java:108) ~[spring-boot-test-3.2.1.jar:3.2.1]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContextInternal(DefaultCacheAwareContextLoaderDelegate.java:225) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.cache.DefaultCacheAwareContextLoaderDelegate.loadContext(DefaultCacheAwareContextLoaderDelegate.java:152) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DefaultTestContext.getApplicationContext(DefaultTestContext.java:130) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.injectDependencies(DependencyInjectionTestExecutionListener.java:141) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.support.DependencyInjectionTestExecutionListener.prepareTestInstance(DependencyInjectionTestExecutionListener.java:97) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.TestContextManager.prepareTestInstance(TestContextManager.java:260) ~[spring-test-6.1.2.jar:6.1.2]
        at org.springframework.test.context.junit.jupiter.SpringExtension.postProcessTestInstance(SpringExtension.java:163) ~[spring-test-6.1.2.jar:6.1.2]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$10(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.executeAndMaskThrowable(ClassBasedTestDescriptor.java:383) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$invokeTestInstancePostProcessors$11(ClassBasedTestDescriptor.java:378) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.stream.ReferencePipeline$3$1.accept(ReferencePipeline.java:197) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$2$1.accept(ReferencePipeline.java:179) ~[na:na]
        at java.base/java.util.ArrayList$ArrayListSpliterator.forEachRemaining(ArrayList.java:1708) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.copyInto(AbstractPipeline.java:509) ~[na:na]
        at java.base/java.util.stream.AbstractPipeline.wrapAndCopyInto(AbstractPipeline.java:499) ~[na:na]
        at java.base/java.util.stream.StreamSpliterators$WrappingSpliterator.forEachRemaining(StreamSpliterators.java:310) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:735) ~[na:na]
        at java.base/java.util.stream.Streams$ConcatSpliterator.forEachRemaining(Streams.java:734) ~[na:na]
        at java.base/java.util.stream.ReferencePipeline$Head.forEach(ReferencePipeline.java:762) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.invokeTestInstancePostProcessors(ClassBasedTestDescriptor.java:377) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$instantiateAndPostProcessTestInstance$6(ClassBasedTestDescriptor.java:290) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.instantiateAndPostProcessTestInstance(ClassBasedTestDescriptor.java:289) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$4(ClassBasedTestDescriptor.java:279) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at java.base/java.util.Optional.orElseGet(Optional.java:364) ~[na:na]
        at org.junit.jupiter.engine.descriptor.ClassBasedTestDescriptor.lambda$testInstancesProvider$5(ClassBasedTestDescriptor.java:278) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.execution.TestInstancesProvider.getTestInstances(TestInstancesProvider.java:31) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.lambda$prepare$0(TestMethodTestDescriptor.java:106) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:105) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.jupiter.engine.descriptor.TestMethodTestDescriptor.prepare(TestMethodTestDescriptor.java:69) ~[junit-jupiter-engine-5.10.1.jar:5.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$prepare$2(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.prepare(NodeTestTask.java:123) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:90) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at java.base/java.util.ArrayList.forEach(ArrayList.java:1596) ~[na:na]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.invokeAll(SameThreadHierarchicalTestExecutorService.java:41) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$6(NodeTestTask.java:155) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$8(NodeTestTask.java:141) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.Node.around(Node.java:137) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.lambda$executeRecursively$9(NodeTestTask.java:139) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.ThrowableCollector.execute(ThrowableCollector.java:73) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.executeRecursively(NodeTestTask.java:138) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.NodeTestTask.execute(NodeTestTask.java:95) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.SameThreadHierarchicalTestExecutorService.submit(SameThreadHierarchicalTestExecutorService.java:35) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestExecutor.execute(HierarchicalTestExecutor.java:57) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.engine.support.hierarchical.HierarchicalTestEngine.execute(HierarchicalTestEngine.java:54) ~[junit-platform-engine-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:198) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:169) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:93) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.lambda$execute$0(EngineExecutionOrchestrator.java:58) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.withInterceptedStreams(EngineExecutionOrchestrator.java:141) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.EngineExecutionOrchestrator.execute(EngineExecutionOrchestrator.java:57) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:103) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DefaultLauncher.execute(DefaultLauncher.java:85) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.junit.platform.launcher.core.DelegatingLauncher.execute(DelegatingLauncher.java:47) ~[junit-platform-launcher-1.10.1.jar:1.10.1]
        at org.apache.maven.surefire.junitplatform.LazyLauncher.execute(LazyLauncher.java:56) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.execute(JUnitPlatformProvider.java:184) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invokeAllTests(JUnitPlatformProvider.java:148) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.junitplatform.JUnitPlatformProvider.invoke(JUnitPlatformProvider.java:122) ~[surefire-junit-platform-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.runSuitesInProcess(ForkedBooter.java:385) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.execute(ForkedBooter.java:162) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.run(ForkedBooter.java:507) ~[surefire-booter-3.2.3.jar:3.2.3]
        at org.apache.maven.surefire.booter.ForkedBooter.main(ForkedBooter.java:495) ~[surefire-booter-3.2.3.jar:3.2.3]
Caused by: org.hibernate.service.spi.ServiceException: Unable to create requested service [org.hibernate.engine.jdbc.env.spi.JdbcEnvironment] due to: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:276) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.initializeService(AbstractServiceRegistryImpl.java:238) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.getService(AbstractServiceRegistryImpl.java:215) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.relational.Database.<init>(Database.java:45) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.getDatabase(InFlightMetadataCollectorImpl.java:223) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.internal.InFlightMetadataCollectorImpl.<init>(InFlightMetadataCollectorImpl.java:191) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.model.process.spi.MetadataBuildingProcess.complete(MetadataBuildingProcess.java:170) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.metadata(EntityManagerFactoryBuilderImpl.java:1432) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.jpa.boot.internal.EntityManagerFactoryBuilderImpl.build(EntityManagerFactoryBuilderImpl.java:1503) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.springframework.orm.jpa.vendor.SpringHibernateJpaPersistenceProvider.createContainerEntityManagerFactory(SpringHibernateJpaPersistenceProvider.java:75) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.createNativeEntityManagerFactory(LocalContainerEntityManagerFactoryBean.java:376) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.buildNativeEntityManagerFactory(AbstractEntityManagerFactoryBean.java:409) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.AbstractEntityManagerFactoryBean.afterPropertiesSet(AbstractEntityManagerFactoryBean.java:396) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.orm.jpa.LocalContainerEntityManagerFactoryBean.afterPropertiesSet(LocalContainerEntityManagerFactoryBean.java:352) ~[spring-orm-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.invokeInitMethods(AbstractAutowireCapableBeanFactory.java:1820) ~[spring-beans-6.1.2.jar:6.1.2]
        at org.springframework.beans.factory.support.AbstractAutowireCapableBeanFactory.initializeBean(AbstractAutowireCapableBeanFactory.java:1769) ~[spring-beans-6.1.2.jar:6.1.2]
        ... 95 common frames omitted
Caused by: org.hibernate.boot.registry.selector.spi.StrategySelectionException: Unable to resolve name [org.hibernate.dialect.SQLiteDialect] as strategy [org.hibernate.dialect.Dialect]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:154) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:236) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.resolveStrategy(StrategySelectorImpl.java:189) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.constructDialect(DialectFactoryImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.dialect.internal.DialectFactoryImpl.buildDialect(DialectFactoryImpl.java:88) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentWithDefaults(JdbcEnvironmentInitiator.java:143) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.getJdbcEnvironmentUsingJdbcMetadata(JdbcEnvironmentInitiator.java:348) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:107) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.engine.jdbc.env.internal.JdbcEnvironmentInitiator.initiateService(JdbcEnvironmentInitiator.java:68) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.internal.StandardServiceRegistryImpl.initiateService(StandardServiceRegistryImpl.java:129) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.service.internal.AbstractServiceRegistryImpl.createService(AbstractServiceRegistryImpl.java:263) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 110 common frames omitted
Caused by: org.hibernate.boot.registry.classloading.spi.ClassLoadingException: Unable to load class [org.hibernate.dialect.SQLiteDialect]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:126) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at org.hibernate.boot.registry.selector.internal.StrategySelectorImpl.selectStrategyImplementor(StrategySelectorImpl.java:150) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 120 common frames omitted
Caused by: java.lang.ClassNotFoundException: Could not load requested class : org.hibernate.dialect.SQLiteDialect
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:216) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:593) ~[na:na]
        at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
        at java.base/java.lang.Class.forName0(Native Method) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:534) ~[na:na]
        at java.base/java.lang.Class.forName(Class.java:513) ~[na:na]
        at org.hibernate.boot.registry.classloading.internal.ClassLoaderServiceImpl.classForName(ClassLoaderServiceImpl.java:123) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 121 common frames omitted
Caused by: java.lang.Throwable: null
        at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:209) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
        ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted
        Suppressed: java.lang.ClassNotFoundException: org.hibernate.dialect.SQLiteDialect
                at java.base/jdk.internal.loader.BuiltinClassLoader.loadClass(BuiltinClassLoader.java:641) ~[na:na]
                at java.base/jdk.internal.loader.ClassLoaders$AppClassLoader.loadClass(ClassLoaders.java:188) ~[na:na]
                at java.base/java.lang.ClassLoader.loadClass(ClassLoader.java:526) ~[na:na]
                at org.hibernate.boot.registry.classloading.internal.AggregatedClassLoader.findClass(AggregatedClassLoader.java:206) ~[hibernate-core-6.4.1.Final.jar:6.4.1.Final]
                ... 127 common frames omitted

---

_**Assistant**_

The error indicates that Hibernate cannot find the `org.hibernate.dialect.SQLiteDialect` class. This is because Hibernate does not provide a built-in SQLite dialect. You need to use a custom SQLite dialect or a third-party library that provides one.

Since you previously had a custom `SQLiteDialect` class, let's revert to using it. Ensure that your custom dialect is correctly implemented and available in the classpath.

### Steps to Resolve:

1. **Revert to Custom SQLiteDialect:**

   Update your `application-test.properties` to use your custom dialect:

   ```properties:src/test/resources/application-test.properties
   # JPA Configuration
   spring.jpa.database-platform=com.langportal.config.SQLiteDialect
   spring.jpa.hibernate.ddl-auto=create-drop
   spring.jpa.generate-ddl=true
   spring.jpa.defer-datasource-initialization=true
   spring.jpa.show-sql=true
   spring.jpa.properties.hibernate.format_sql=true
   spring.jpa.properties.hibernate.dialect=com.langportal.config.SQLiteDialect
   spring.jpa.properties.hibernate.id.new_generator_mappings=false
   ```

2. **Ensure Custom Dialect is Correctly Implemented:**

   Make sure your `SQLiteDialect` class is correctly implemented and located in `src/main/java/com/langportal/config/`. The class should extend `Dialect` and be compatible with Hibernate 6.

3. **Verify Classpath:**

   Ensure that your custom `SQLiteDialect` class is being compiled and included in the classpath. You can check this by looking for `SQLiteDialect.class` in `target/classes/com/langportal/config/`.

4. **Add SQLite JDBC Driver Dependency:**

   Ensure you have the SQLite JDBC driver in your `pom.xml`:

   ```xml
   <dependency>
       <groupId>org.xerial</groupId>
       <artifactId>sqlite-jdbc</artifactId>
       <version>3.45.1.0</version>
       <scope>test</scope>
   </dependency>
   ```

5. **Rebuild the Project:**

   After making these changes, clean and rebuild your project to ensure all changes are applied.

If you follow these steps and ensure your custom dialect is correctly implemented and available, the issue should be resolved. If you encounter further issues, please provide the implementation of your `SQLiteDialect` class for further assistance.

---

_**User**_

how do I overwrite all local changes from git

---

_**Assistant**_

To overwrite all local changes in your Git repository and reset it to the state of the remote repository, you can use the following steps. Be cautious, as this will discard all local changes, including uncommitted changes and local commits that haven't been pushed.

1. **Stash or Discard Uncommitted Changes:**

   If you have uncommitted changes that you want to keep, you can stash them. Otherwise, you can skip this step if you want to discard them.

   ```bash
   git stash
   ```

2. **Fetch the Latest Changes from the Remote:**

   This will update your local repository with the latest changes from the remote repository.

   ```bash
   git fetch origin
   ```

3. **Reset Your Local Branch to Match the Remote:**

   This command will reset your current branch to match the remote branch, discarding all local changes.

   ```bash
   git reset --hard origin/main
   ```

   Replace `main` with the name of your branch if it's different.

4. **Clean Untracked Files and Directories:**

   If you also want to remove untracked files and directories, use the following command:

   ```bash
   git clean -fd
   ```

   The `-f` flag is for force, and `-d` is for directories.

### Important Notes:

- **Data Loss Warning:** These commands will permanently delete all local changes that are not committed or stashed. Ensure you have backups of any important work.
- **Branch Name:** Make sure to replace `main` with the correct branch name if your default branch is named differently (e.g., `master` or another branch name).

By following these steps, your local repository will be reset to match the state of the remote repository, effectively discarding all local changes.

---



---

